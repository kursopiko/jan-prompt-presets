"""
ComfyUI Custom Node: Text Split
Splits a multiline string into a list of strings, one per non-empty line.
"""


class TextSplitNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "text": ("STRING", {
                    "multiline": True,
                    "default": "",
                    "tooltip": "Each non-empty line becomes one element in the output list.",
                }),
                "skip_empty_lines": ("BOOLEAN", {
                    "default": True,
                    "tooltip": "When enabled, blank lines are excluded from the output list.",
                }),
            },
        }

    RETURN_TYPES = ("STRING_LIST",)
    RETURN_NAMES = ("list",)
    FUNCTION = "split"
    CATEGORY = "prompt/presets"
    OUTPUT_NODE = False

    def split(self, text: str, skip_empty_lines: bool):
        lines = text.splitlines()
        if skip_empty_lines:
            lines = [l for l in lines if l.strip()]
        return (lines,)


# --- ComfyUI Registration ---

NODE_CLASS_MAPPINGS = {
    "TextSplitNode": TextSplitNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "TextSplitNode": "Text Split",
}
