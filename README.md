# ComfyUI-Extract_Flux_Lora
Extract LoRA from the original Fine-Tuned model.从微调模型中提取lora。

此节点来自[ComfyUI-FluxTrainer](https://github.com/kijai/ComfyUI-FluxTrainer)，用来从各种微调模型中提取lora。根据此[issue](https://github.com/kijai/ComfyUI-FluxTrainer/issues/65)修复了一个bug，原节点有些微调模型无法用来转换。注意，如果你已经安装了[ComfyUI-FluxTrainer](https://github.com/kijai/ComfyUI-FluxTrainer)，那么为避免冲突你可以将本项目的flux_extract_lora.py代替[ComfyUI-FluxTrainer](https://github.com/kijai/ComfyUI-FluxTrainer)里的同名文件。之所以提取lora，是因为目前[nunchaku](https://github.com/mit-han-lab/ComfyUI-nunchaku)只能使用原版flux模型的svdq模型，无法使用其他微调过的模型。用此节点提取的lora可以与svdq模型一起使用，拥有svdquant的速度与显存占用，且效果与原微调模型比较接近，是[nunchaku](https://github.com/mit-han-lab/ComfyUI-nunchaku)放出模型量化的节点前的临时替代方法。当然如果不在意差异，提取lora也可以代替原版微调模型，节省空间。提取的lora与原版模型对比结果如下图，对比用的lora的rank为128，适当提高强度能使得lora效果更接近原微调模型，详细内容可参考此文章[reddit](https://www.reddit.com/r/DreamBooth/comments/1fk95s1/how_to_extract_lora_from_flux_fine_tuning/)

![图片11](https://github.com/user-attachments/assets/2cf2c190-4ce9-422d-815b-8724108ebe25)


