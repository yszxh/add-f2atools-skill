---
name: f2atools
description: Interface with YYDS API for AI image/video generation. Supports text-to-image, image-to-image (base64), and model selection.
# EXTENDED METADATA (MANDATORY)
github_url: https://github.com/YoKONCy/f2aTools
github_hash: f75adcd78195cdc66d32901298327c433fa4c81d
version: 0.1.0
created_at: 2026-01-28
entry_point: scripts/generate.py
dependencies: ["requests"]
---

# f2aTools Skill

This skill allows Claude to generate images and videos using the YYDS API service.

## Core Capabilities

1.  **Text to Image/Video**: Generate visuals from a text prompt.
2.  **Image to Image/Video**: Use a reference image (local path) for generation.
3.  **Model Selection**: Choose from various Gemini, Imagen, and Veo models.
4.  **Batch Generation**: Support for multiple concurrent requests.

## Usage

### Simple Generation
"Generate an image of a cyberpunk city using f2atools"
Trigger: `/f2atools generate --prompt "cyberpunk city"`

### Using a Reference Image
"Use this image to generate a futuristic version: path/to/image.jpg"
Trigger: `/f2atools generate --prompt "futuristic version" --image_path "path/to/image.jpg"`

### Specifying a Model
"Generate a 15-second video of a cat dancing using veo_2_1_fast"
Trigger: `/f2atools generate --prompt "cat dancing" --model "veo_2_1_fast_d_15_t2v_landscape"`

## Configuration

This skill requires `F2A_API_BASE_URL` and `F2A_API_KEY` to be set in the environment or passed as arguments.

## Models (Examples)

- **Images**:
    - `gemini-2.5-flash-image-landscape`
    - `gemini-3.0-pro-image-portrait`
    - `imagen-4.0-generate-preview-landscape`
- **Videos**:
    - `veo_3_1_t2v_fast_landscape`
    - `veo_2_1_fast_d_15_t2v_portrait`

## Best Practices

- Always provide a descriptive prompt.
- For video generation, use the appropriate `veo` models.
- If a generation fails or returns a violation, try refining the prompt.
