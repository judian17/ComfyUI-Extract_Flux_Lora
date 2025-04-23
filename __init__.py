from .extract_lora_node import ExtractFluxLoRA

NODE_CLASS_MAPPINGS = {
    "ExtractFluxLoRA": ExtractFluxLoRA
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExtractFluxLoRA": "Extract Flux LoRA"
}

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]