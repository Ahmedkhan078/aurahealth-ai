import numpy as np
try:
    try:
    from scipy.optimize import linprog
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False
from pydantic import BaseModel
from typing import List, Dict

class FoodItem(BaseModel):
    name: str
    cost: float
    glycemic_index: float
    protein: float
    carbs: float
    fat: float
    calories: float

class NutritionalTarget(BaseModel):
    protein: float
    carbs: float
    fat: float
    calories: float

def optimize_meal_plan(foods: List[FoodItem], target: NutritionalTarget, budget: float, max_gi: float) -> Dict:
    """
    Metabolic Optimizer: Uses Linear Programming to minimize the gap between
    a target nutritional profile and the chosen foods, subject to budget and GI constraints.
    """
    if not SCIPY_AVAILABLE:
        # Mock successful response for local development without scipy
        return {
            "feasible": True,
            "total_cost": 10.50,
            "plan": [
                {"food": "Mock Chicken Breast", "quantity": 1.5},
                {"food": "Mock Brown Rice", "quantity": 2.0}
            ],
            "message": "Note: Using MOCK data because scipy is not installed locally."
        }

    if not foods:
        raise ValueError("Food list cannot be empty.")

    n_foods = len(foods)
    
    # Objective: Minimize cost
    c = [food.cost for food in foods]
    
    # Inequality constraints: A_ub * x <= b_ub
    # 1. Budget constraint: sum(x_i * cost_i) <= budget (redundant with objective but good to enforce)
    # 2. Glycemic constraint: sum(x_i * gi_i) <= max_gi 
    # (Note: A true GI constraint is usually weighted by carbs, but we keep it simple here)
    A_ub = [
        [food.cost for food in foods],
        [food.glycemic_index for food in foods]
    ]
    b_ub = [budget, max_gi]
    
    # Equality constraints: A_eq * x == b_eq
    # Meet macro targets exactly (or relax to inequality for real-world)
    A_eq = [
        [food.protein for food in foods],
        [food.carbs for food in foods],
        [food.fat for food in foods],
        [food.calories for food in foods]
    ]
    b_eq = [target.protein, target.carbs, target.fat, target.calories]
    
    # Bounds: Can't have negative food quantities
    bounds = [(0, None) for _ in range(n_foods)]
    
    # Solve linear program
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='highs')
    
    if res.success:
        plan = []
        for i, qty in enumerate(res.x):
            if qty > 1e-5: # Filter out near-zero quantities
                plan.append({
                    "food": foods[i].name,
                    "quantity": round(qty, 2)
                })
        return {
            "feasible": True,
            "total_cost": round(res.fun, 2),
            "plan": plan
        }
    else:
        return {
            "feasible": False,
            "message": "Could not find a plan meeting all constraints.",
            "details": res.message
        }
