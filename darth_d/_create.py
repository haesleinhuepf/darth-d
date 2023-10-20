from stackview import jupyter_displayable_output

@jupyter_displayable_output(library_name='darth-d', help_url='https://github.com/haesleinhuepf/darth-d')
def create(prompt:str=None, image_size:int=256, num_images:int=1):

    import openai
    
    from ._utilities import images_from_url_responses

    response = openai.Image.create(
      prompt=prompt,
      n=num_images,
      size=f"{image_size}x{image_size}"
    )
    
    return images_from_url_responses(response)
