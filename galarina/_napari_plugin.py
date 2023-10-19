
from napari_plugin_engine import napari_hook_implementation

@napari_hook_implementation
def napari_experimental_provide_function():
    return [gala_gui]


from napari_tools_menu import register_function

@register_function(menu="Generate > Image")
def gala_gui(prompt:str, image_size:int=256, num_images:int = 1) -> "napari.types.ImageData":
    from ._gala import galarina

    image = galarina(prompt=prompt, image_size=image_size, num_images=num_images)

    return image

