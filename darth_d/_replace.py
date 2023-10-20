from stackview import jupyter_displayable_output

@jupyter_displayable_output(library_name='darth-d', help_url='https://github.com/haesleinhuepf/darth-d')
def replace(input_image, mask = None, prompt:str = "A similar pattern like in the rest of the image", image_size:int=256, num_images:int = 1):
    from ._utilities import numpy_to_bytestream
    from stackview._image_widget import _img_to_rgb
    from skimage import transform
    import numpy as np
    import openai
    from ._utilities import images_from_url_responses

    if mask is None:
        mask = np.zeros(input_image.shape[:2], dtype=np.uint8)
        mask[:int(mask.shape[0] / 2), :int(mask.shape[1] / 2)] = 1
        mask[int(mask.shape[0] / 2):, int(mask.shape[1] / 2):] = 1

        half_replaced = replace(input_image=input_image, mask=mask, prompt=prompt, image_size=image_size, num_images=num_images)
        mask_inverse = ((mask == 0) * 1).astype(dtype=np.uint8)

        if num_images > 1:
            replaced = np.asarray([
                replace(input_image=half_replaced_image, mask=mask_inverse, prompt=prompt, image_size=image_size,
                        num_images=1) for half_replaced_image in half_replaced])
        else:
            replaced = replace(input_image=half_replaced, mask=mask_inverse, prompt=prompt, image_size=image_size,
                        num_images=num_images)

        return replaced

    resized_image = transform.resize(input_image, (image_size, image_size), anti_aliasing=True)
    resized_mask = transform.resize(mask, (image_size, image_size), anti_aliasing=False)
    
    masked = np.swapaxes(np.swapaxes(np.asarray([(resized_mask == 0)] * 4), 0, 2), 0,1)
    
    response = openai.Image.create_edit(
      image=numpy_to_bytestream(_img_to_rgb(resized_image)),
      mask=numpy_to_bytestream(masked),
      prompt=prompt,
      n=num_images,
      size=f"{image_size}x{image_size}"
    )
    return images_from_url_responses(response, input_image.shape)
    