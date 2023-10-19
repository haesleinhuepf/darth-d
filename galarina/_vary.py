def vary(input_image, image_size:int=256, num_images:int = 1):
    import openai
    from ._utilities import numpy_to_bytestream
    from ._utilities import images_from_url_responses
    
    from stackview._image_widget import _img_to_rgb
    
    response = openai.Image.create_variation(
      image=numpy_to_bytestream(_img_to_rgb(input_image)),
      n=num_images,
      size=f"{image_size}x{image_size}"
    )
    return images_from_url_responses(response, input_image.shape)
    