"""
ComfyUI Custom Node: Lighting Presets
Provides a dropdown of predefined SDXL lighting presets with an optional custom override.

Installation:
  Place this file in: ComfyUI/custom_nodes/lighting_presets_node.py
  Restart ComfyUI.
"""

LIGHTING_PRESETS = {
    "None / Custom": "",

    "Dramatic": (
        "dramatic lighting, strong directional light, deep harsh shadows, high contrast, "
        "chiaroscuro, single hard light source, intense atmosphere"
    ),

    "Cinematic": (
        "cinematic lighting, three-point lighting setup, motivated light sources, "
        "subtle color grading, anamorphic lens flare, film-like quality, professional cinematography"
    ),

    "Golden Hour": (
        "golden hour lighting, warm golden sunlight, long soft shadows, "
        "rich amber and orange tones, sun low on horizon, glowing rim light, magical hour"
    ),

    "Neon Night": (
        "neon night lighting, vibrant neon signs, cyan and magenta light spill, "
        "wet reflective streets, deep shadows punctuated by colored light, cyberpunk atmosphere, "
        "harsh artificial light sources"
    ),

    "Moody Thriller": (
        "moody thriller lighting, low key lighting, deep shadows, cool desaturated tones, "
        "single motivated light source, noir atmosphere, tension and unease, "
        "pools of light in darkness, film noir style"
    ),

    "Soft Natural Daylight": (
        "soft natural daylight, diffused overcast light, even illumination, "
        "no harsh shadows, gentle fill light, clean neutral tones, bright airy atmosphere"
    ),

    "Moonlit Night": (
        "moonlit night, cool pale blue moonlight, soft directional light from above, "
        "long gentle shadows, silver and deep blue tones, quiet serene atmosphere, "
        "stars visible, subtle ambient glow"
    ),

    "Studio": (
        "studio lighting, professional softbox lighting, clean white background, "
        "controlled even illumination, product photography quality, "
        "subtle shadow for depth, crisp and polished"
    ),
}


class LightingPresetsNode:
    """
    A ComfyUI node that outputs a predefined SDXL lighting preset prompt string.
    If a custom override is provided, it takes priority over the dropdown selection.
    """

    @classmethod
    def INPUT_TYPES(cls):
        preset_names = list(LIGHTING_PRESETS.keys())
        return {
            "required": {
                "preset": (preset_names, {
                    "default": "None / Custom",
                    "tooltip": "Select a predefined lighting preset for your SDXL prompt.",
                }),
            },
            "optional": {
                "custom_override": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "placeholder": "Enter a custom lighting prompt here to override the dropdown selection...",
                    "tooltip": "If filled, this overrides the dropdown selection entirely.",
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("lighting_prompt",)
    FUNCTION = "get_lighting_prompt"
    CATEGORY = "prompt/presets"
    OUTPUT_NODE = False

    def get_lighting_prompt(self, preset: str, custom_override: str = ""):
        override = custom_override.strip()
        if override:
            return (override,)

        prompt = LIGHTING_PRESETS.get(preset, "")
        return (prompt,)


# --- ComfyUI Registration ---

NODE_CLASS_MAPPINGS = {
    "LightingPresetsNode": LightingPresetsNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "LightingPresetsNode": "Lighting Presets",
}
