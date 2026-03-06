CAMERA_PRESETS = {
    "None / Custom": "",
    "Cinematic Hero": "low angle, dramatic perspective, cinematic framing, foreshortening",
    "Dynamic Action": "dutch angle, dynamic perspective, tilted camera, wide angle lens",
    "Intimate Portrait": "close-up, eye level, shallow depth of field, portrait",
    "Character Showcase": "full body, eye level, centered composition",
    "Over-the-Shoulder Scene": "over the shoulder, medium shot, depth of field",
    "Epic Wide Scene": "wide shot, low angle, wide angle lens, cinematic framing"
}


class CameraPresetsNode:
    """
    A ComfyUI node that outputs a predefined SDXL camera/shot preset prompt string.
    If a custom override is provided, it takes priority over the dropdown selection.
    """

    @classmethod
    def INPUT_TYPES(cls):
        preset_names = list(CAMERA_PRESETS.keys())
        return {
            "required": {
                "preset": (preset_names, {
                    "default": "None / Custom",
                    "tooltip": "Select a predefined camera/shot preset for your SDXL prompt.",
                }),
            },
            "optional": {
                "custom_override": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Enter a custom camera prompt here to override the dropdown selection...",
                    "tooltip": "If filled, this overrides the dropdown selection entirely.",
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("camera_prompt",)
    FUNCTION = "get_camera_prompt"
    CATEGORY = "prompt/presets"
    OUTPUT_NODE = False

    def get_camera_prompt(self, preset: str, custom_override: str = ""):
        # Custom override takes full priority if provided
        override = custom_override.strip()
        if override:
            return (override,)

        prompt = CAMERA_PRESETS.get(preset, "")
        return (prompt,)


# --- ComfyUI Registration ---

NODE_CLASS_MAPPINGS = {
    "CameraPresetsNode": CameraPresetsNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "CameraPresetsNode": "Camera Presets",
}
