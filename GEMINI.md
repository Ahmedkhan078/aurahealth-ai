# AuraHealth AI - Gemini Agent Guidelines

## Rule 1: Always stay on the 'main' branch
All agentic interactions, bug fixes, and feature additions must be committed directly to the `main` branch. This enforces a rapid, single-stream continuous deployment pipeline.

## Rule 2: Keep repository < 1MB
Before marking any task as complete, you must ensure the repository size remains under 1MB. This means:
- Remove all logs and temporary files.
- Exclude large assets (images, datasets, node_modules, compiled binaries).
- Ensure `.gitignore` is strictly enforced.

## Rule 3: Use Gemini 3 Flash for all multimodal reasoning
Whenever volumetric food estimation, macro identification from images, or multimodal prompt parsing is required, you must route these requests through the `Vision Agent` which utilizes Vertex AI's Gemini 3 Flash model.
