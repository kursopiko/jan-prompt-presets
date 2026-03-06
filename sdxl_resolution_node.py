"""
ComfyUI Custom Node: SDXL Resolution Picker
Provides a dropdown of the most common SDXL-optimized resolutions.
Outputs width and height as integers.
"""

# Format: "Label": (width, height)
SDXL_RESOLUTIONS = {
    "1024 x 1024  (1:1 Square)":     (1024, 1024),
    "1152 x 896   (9:7 Landscape)":  (1152, 896),
    "1216 x 832   (3:2 Landscape)":  (1216, 832),
    "1344 x 768   (16:9 Landscape)": (1344, 768),
    "1536 x 640   (12:5 Wide)":      (1536, 640),
    "896 x 1152   (7:9 Portrait)":   (896,  1152),
    "832 x 1216   (2:3 Portrait)":   (832,  1216),
    "768 x 1344   (9:16 Portrait)":  (768,  1344),
    "640 x 1536   (5:12 Tall)":      (640,  1536),
}


class SDXLResolutionNode:
    """
    A ComfyUI node that outputs width and height for a selected SDXL resolution.
    """

    @classmethod
    def INPUT_TYPES(cls):
        resolution_names = list(SDXL_RESOLUTIONS.keys())
        return {
            "required": {
                "resolution": (resolution_names, {
                    "default": "1024 x 1024  (1:1 Square)",
                    "tooltip": "Select a common SDXL-optimised resolution.",
                }),
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_resolution"
    CATEGORY = "prompt/presets"
    OUTPUT_NODE = False

    def get_resolution(self, resolution: str):
        width, height = SDXL_RESOLUTIONS.get(resolution, (1024, 1024))
        return (width, height)


# --- ComfyUI Registration ---

NODE_CLASS_MAPPINGS = {
    "SDXLResolutionNode": SDXLResolutionNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SDXLResolutionNode": "SDXL Resolution Picker",
}
