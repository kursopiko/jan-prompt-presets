# jan-prompt-presets

A collection of small utility nodes for ComfyUI that make common prompt-building and sampler configuration tasks faster. All nodes live under the **`prompt/presets`** category.

---

## Nodes

### Camera Presets
Outputs a prompt string for common camera angles and shot types.

| Option | Description |
|---|---|
| None / Custom | Empty output — use the custom override field |
| Cinematic Hero | Low angle, dramatic perspective, foreshortening |
| Dynamic Action | Dutch angle, tilted camera, wide angle lens |
| Intimate Portrait | Close-up, eye level, shallow depth of field |
| Character Showcase | Full body, eye level, centered composition |
| Over-the-Shoulder Scene | OTS framing, medium shot, depth of field |
| Epic Wide Scene | Wide shot, low angle, cinematic framing |

**Output:** `camera_prompt` (STRING)
**Optional input:** `custom_override` — if filled, replaces the dropdown entirely.

---

### Lighting Presets
Outputs a prompt string for common lighting setups.

| Option | Description |
|---|---|
| None / Custom | Empty output — use the custom override field |
| Dramatic | Strong directional light, deep shadows, chiaroscuro |
| Cinematic | Three-point lighting, colour grading, anamorphic flare |
| Golden Hour | Warm sunlight, long soft shadows, amber tones |
| Neon Night | Vibrant neon, cyan/magenta spill, cyberpunk atmosphere |
| Moody Thriller | Low key, cool tones, noir atmosphere |
| Soft Natural Daylight | Diffused overcast light, even illumination, airy feel |
| Moonlit Night | Cool pale moonlight, silver and deep blue tones |
| Studio | Professional softbox, clean white background |

**Output:** `lighting_prompt` (STRING)
**Optional input:** `custom_override` — if filled, replaces the dropdown entirely.

---

### SDXL Resolution Picker
Outputs width and height for all standard SDXL bucket resolutions (the aspect ratios the model was trained on).

| Option | Resolution |
|---|---|
| 1024 x 1024 (1:1 Square) | 1024 × 1024 |
| 1152 x 896 (9:7 Landscape) | 1152 × 896 |
| 1216 x 832 (3:2 Landscape) | 1216 × 832 |
| 1344 x 768 (16:9 Landscape) | 1344 × 768 |
| 1536 x 640 (12:5 Wide) | 1536 × 640 |
| 896 x 1152 (7:9 Portrait) | 896 × 1152 |
| 832 x 1216 (2:3 Portrait) | 832 × 1216 |
| 768 x 1344 (9:16 Portrait) | 768 × 1344 |
| 640 x 1536 (5:12 Tall) | 640 × 1536 |

**Outputs:** `width` (INT), `height` (INT)

---

### Scheduler Selector
A clean dropdown for picking a scheduler, sourced directly from ComfyUI's core (`comfy.samplers.KSampler.SCHEDULERS`). Automatically includes any schedulers added by other installed packages.

**Output:** `scheduler` — type-compatible with the scheduler input on KSampler and similar nodes.

---

### Sampler Selector
Same as Scheduler Selector but for samplers, sourced from `comfy.samplers.KSampler.SAMPLERS`.

**Output:** `sampler_name` — type-compatible with the sampler input on KSampler and similar nodes.

---

### Text Split
Splits a multiline string into a list, one element per line.

**Input:** `text` (STRING, multiline), `skip_empty_lines` (BOOLEAN, default: true)
**Output:** `list` (STRING_LIST)

---

### List Get Index
Returns a single element from a `STRING_LIST` by index. Supports negative indices (`-1` = last element).

**Input:** `list` (STRING_LIST), `index` (INT)
**Output:** `element` (STRING)

---

## Installation

1. Clone or copy this folder into `ComfyUI/custom_nodes/`:
   ```
   git clone https://github.com/kursopiko/jan-prompt-presets.git
   ```
2. Restart ComfyUI.
3. All nodes will appear under the **`prompt/presets`** category.
