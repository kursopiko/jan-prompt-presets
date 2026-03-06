"""
ComfyUI Custom Node: Scheduler Selector
Provides a dropdown of all available schedulers sourced directly from ComfyUI's
core (comfy.samplers.KSampler.SCHEDULERS), so it stays in sync with whatever
schedulers are installed. Output connects directly to KSampler, FaceDetailer, etc.
"""

import comfy.samplers


class SchedulerSelectorNode:
    """
    A ComfyUI node that exposes a scheduler dropdown whose output is
    compatible with the scheduler input on KSampler and similar nodes.
    """

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "scheduler": (comfy.samplers.KSampler.SCHEDULERS, {
                    "default": "karras",
                    "tooltip": "Select a scheduler to use with KSampler, FaceDetailer, etc.",
                }),
            },
        }

    # Using the same list as the return type lets ComfyUI match it to
    # any input that also accepts KSampler.SCHEDULERS (i.e. scheduler slots).
    RETURN_TYPES = (comfy.samplers.KSampler.SCHEDULERS,)
    RETURN_NAMES = ("scheduler",)
    FUNCTION = "get_scheduler"
    CATEGORY = "prompt/presets"
    OUTPUT_NODE = False

    def get_scheduler(self, scheduler: str):
        return (scheduler,)


# --- ComfyUI Registration ---

NODE_CLASS_MAPPINGS = {
    "SchedulerSelectorNode": SchedulerSelectorNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SchedulerSelectorNode": "Scheduler Selector",
}
