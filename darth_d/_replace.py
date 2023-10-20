from stackview import jupyter_displayable_output

@jupyter_displayable_output(library_name='darth-d', help_url='https://github.com/haesleinhuepf/darth-d')
def replace(input_image, mask, prompt:str, image_size:int=256, num_images:int = 1):
    from ._utilities import numpy_to_bytestream
    from stackview._image_widget import _img_to_rgb
    from skimage import transform
    import numpy as np
    import openai
    from ._utilities import images_from_url_responses
    
    resized_image = transform.resize(input_image, (256, 256), anti_aliasing=True)
    resized_mask = transform.resize(mask, (256, 256), anti_aliasing=True)
    
    masked = np.swapaxes(np.swapaxes(np.asarray([(resized_mask == 0)] * 4), 0, 2), 0,1)
    
    response = openai.Image.create_edit(
      image=numpy_to_bytestream(_img_to_rgb(resized_image)),
      mask=numpy_to_bytestream(masked),
      prompt=prompt,
      n=num_images,
      size=f"{image_size}x{image_size}"
    )
    return images_from_url_responses(response, input_image.shape)
    