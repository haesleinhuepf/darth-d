
from napari_plugin_engine import napari_hook_implementation

@napari_hook_implementation
def napari_experimental_provide_function():
    return [create_gui, vary_gui]


from napari_tools_menu import register_function

@register_function(menu="Generate > Create new image (DALL-E 2, OpenAI, Darth-D)")
def create_gui(prompt:str, image_size:int=256, num_images:int = 1) -> "napari.types.ImageData":
    from ._create import create

    image = create(prompt=prompt, image_size=image_size, num_images=num_images)

    return image

@register_function(menu="Generate > Vary image (DALL-E 2, OpenAI, Darth-D)")
def vary_gui(input_image:"napari.types.ImageData", image_size:int=256, num_images:int = 1) -> "napari.types.ImageData":
    from ._vary import vary

    image = vary(input_image=input_image, image_size=image_size, num_images=num_images)

    return image
    

@register_function(menu="Generate > Replace masked region (DALL-E 2, OpenAI, Darth-D)")
def vary_gui(input_image:"napari.types.ImageData", mask:"napari.types.LabelsData", prompt:str, image_size:int=256, num_images:int = 1) -> "napari.types.ImageData":
    from ._replace import replace

    image = replace(input_image=input_image, mask=mask, prompt=prompt, image_size=image_size, num_images=num_images)

    return image
    


