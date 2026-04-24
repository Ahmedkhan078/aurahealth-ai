# AuraHealth AI - Agent Directory

## 1. Governance Agent
- **Role**: Ensures adherence to repository constraints (single branch, < 1MB size).
- **Tooling**: Git, filesystem commands.

## 2. Vision Agent (`/api/logic/vision_agent.py`)
- **Role**: Handles multimodal input (images of food) to perform volumetric food estimation and macro identification.
- **Model**: Vertex AI Gemini 3 Flash.

## 3. Metabolic Optimizer (`/api/logic/optimizer.py`)
- **Role**: Computes the optimal meal plan to minimize nutritional gaps.
- **Algorithm**: Linear Programming via `scipy.optimize.linprog`.
- **Constraints**: User budget, glycemic index limits, macro targets.

## 4. Web Agent (Frontend)
- **Role**: Provides the user interface for capturing inputs and displaying optimized plans.
- **Tech**: React, Vite, Tailwind CSS.
