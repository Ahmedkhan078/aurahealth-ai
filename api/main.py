from fastapi import FastAPI, HTTPException, UploadFile, File
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# Import logic modules
from logic.optimizer import optimize_meal_plan, FoodItem, NutritionalTarget
from logic.vision_agent import analyze_food_image

app = FastAPI(title="AuraHealth AI Backend", version="1.0.0")

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # For production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "ok", "agent": "healthy"}

@app.post("/api/analyze-meal")
async def analyze_meal(file: UploadFile = File(...)):
    """
    Endpoint for the Vision Agent to analyze food images.
    """
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File must be an image.")
    
    # Read image bytes
    image_bytes = await file.read()
    
    try:
        analysis_result = analyze_food_image(image_bytes)
        return {"status": "success", "analysis": analysis_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Vision Agent Error: {str(e)}")

class OptimizeRequest(BaseModel):
    foods: List[FoodItem]
    target: NutritionalTarget
    budget: float
    max_glycemic_index: float

@app.post("/api/optimize-plan")
def optimize_plan(req: OptimizeRequest):
    """
    Endpoint for the Metabolic Optimizer to generate meal plans.
    """
    try:
        result = optimize_meal_plan(
            foods=req.foods,
            target=req.target,
            budget=req.budget,
            max_gi=req.max_glycemic_index
        )
        return {"status": "success", "plan": result}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Optimizer Error: {str(e)}")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
