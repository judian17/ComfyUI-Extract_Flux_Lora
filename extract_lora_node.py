import os
import torch
import folder_paths
from pathlib import Path

class ExtractFluxLoRA:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "original_model": (folder_paths.get_filename_list("unet"), ),
                "finetuned_model": (folder_paths.get_filename_list("unet"), ),
                "output_path": ("STRING", {"default": f"{str(os.path.join(folder_paths.models_dir, 'loras', 'Flux'))}"}),
                "dim": ("INT", {"default": 4, "min": 2, "max": 1024, "step": 2, "tooltip": "LoRA rank"}),
                "save_dtype": (["fp32", "fp16", "bf16", "fp8_e4m3fn", "fp8_e5m2"], {"default": "bf16", "tooltip": "the dtype to save the LoRA as"}),
                "load_device": (["cpu", "cuda"], {"default": "cuda", "tooltip": "the device to load the model to"}),
                "store_device": (["cpu", "cuda"], {"default": "cpu", "tooltip": "the device to store the LoRA as"}),
                "clamp_quantile": ("FLOAT", {"default": 0.99, "min": 0.0, "max": 1.0, "step": 0.01, "tooltip": "clamp quantile"}),
                "metadata": ("BOOLEAN", {"default": True, "tooltip": "build metadata"}),
                "mem_eff_safe_open": ("BOOLEAN", {"default": False, "tooltip": "memory efficient loading"}),
             },
        }

    RETURN_TYPES = ("STRING", )
    RETURN_NAMES = ("output_path",)
    FUNCTION = "extract"
    CATEGORY = "FluxTrainer"

    def extract(self, original_model, finetuned_model, output_path, dim, save_dtype, load_device, store_device, clamp_quantile, metadata, mem_eff_safe_open):
        from .flux_extract_lora import svd
        transformer_path = folder_paths.get_full_path("unet", original_model)
        finetuned_model_path = folder_paths.get_full_path("unet", finetuned_model)
        outpath = svd(
            model_org = transformer_path,
            model_tuned = finetuned_model_path,
            save_to = os.path.join(output_path, f"{finetuned_model.replace('.safetensors', '')}_extracted_lora_rank_{dim}-{save_dtype}.safetensors"),
            dim = dim,
            device = load_device,
            store_device = store_device,
            save_precision = save_dtype,
            clamp_quantile = clamp_quantile,
            no_metadata = not metadata,
            mem_eff_safe_open = mem_eff_safe_open
        )
     
        return (outpath,)

NODE_CLASS_MAPPINGS = {
    "ExtractFluxLoRA": ExtractFluxLoRA
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ExtractFluxLoRA": "Extract Flux LoRA"
}