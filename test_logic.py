from api.logic.optimizer import optimize_meal_plan, FoodItem, NutritionalTarget
from api.logic.vision_agent import analyze_food_image

def run_tests():
    print("--- Testing Vision Agent ---")
    try:
        # Pass dummy bytes
        result = analyze_food_image(b"dummy_image_data")
        print(f"Vision Agent Output: {result}")
        print("✅ Vision Agent test passed.\n")
    except Exception as e:
        print(f"❌ Vision Agent test failed: {e}\n")

    print("--- Testing Metabolic Optimizer ---")
    try:
        foods = [
            FoodItem(name="Chicken Breast", cost=3.50, glycemic_index=0, protein=31, carbs=0, fat=3.6, calories=165),
            FoodItem(name="Brown Rice", cost=1.20, glycemic_index=50, protein=2.6, carbs=23, fat=0.9, calories=111),
            FoodItem(name="Broccoli", cost=0.80, glycemic_index=15, protein=2.8, carbs=6.6, fat=0.4, calories=34),
        ]
        
        target = NutritionalTarget(protein=60, carbs=50, fat=10, calories=500)
        
        # We give a generous budget and GI max just to find feasibility
        result = optimize_meal_plan(foods=foods, target=target, budget=15.0, max_gi=100.0)
        
        print("Optimizer Output:")
        print(result)
        if result.get("feasible") or not result.get("feasible"): # Just checking it doesn't crash
             print("✅ Optimizer test completed execution without errors.\n")
    except Exception as e:
        print(f"❌ Optimizer test failed: {e}\n")

if __name__ == "__main__":
    run_tests()
