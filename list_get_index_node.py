"""
ComfyUI Custom Node: List Get Index
Returns the element at the given index from a STRING_LIST.
Supports negative indices (e.g. -1 for the last element).
"""


class ListGetIndexNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "list": ("STRING_LIST", {
                    "tooltip": "The list to read from.",
                }),
                "index": ("INT", {
                    "default": 0,
                    "min": -10000,
                    "max": 10000,
                    "step": 1,
                    "tooltip": "Index of the element to retrieve. Negative values count from the end.",
                }),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("element",)
    FUNCTION = "get_index"
    CATEGORY = "prompt/presets"
    OUTPUT_NODE = False

    def get_index(self, list: list, index: int):
        return (list[index],)


# --- ComfyUI Registration ---

NODE_CLASS_MAPPINGS = {
    "ListGetIndexNode": ListGetIndexNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ListGetIndexNode": "List Get Index",
}
