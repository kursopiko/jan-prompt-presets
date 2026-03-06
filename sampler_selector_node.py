"""
ComfyUI Custom Node: Sampler Selector
Provides a dropdown of all available samplers sourced directly from ComfyUI's
core (comfy.samplers.KSampler.SAMPLERS), so it stays in sync with whatever
samplers are installed. Output connects directly to KSampler, FaceDetailer, etc.
"""

import comfy.samplers


class SamplerSelectorNode:
    """
    A ComfyUI node that exposes a sampler dropdown whose output is
    compatible with the sampler input on KSampler and similar nodes.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "sampler": (comfy.samplers.KSampler.SAMPLERS, {
                    "default": "euler",
                    "tooltip": "Select a sampler to use with KSampler, FaceDetailer, etc.",
                }),
            },
        }

    RETURN_TYPES = (comfy.samplers.KSampler.SAMPLERS,)
    RETURN_NAMES = ("sampler_name",)
    FUNCTION = "get_sampler"
    CATEGORY = "prompt/presets"
    OUTPUT_NODE = False

    def get_sampler(self, sampler: str):
        return (sampler,)


# --- ComfyUI Registration ---

NODE_CLASS_MAPPINGS = {
    "SamplerSelectorNode": SamplerSelectorNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SamplerSelectorNode": "Sampler Selector",
}
