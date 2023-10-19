
def galarina(prompt:str=None, image_size:int=256, num_images:int=1):

    import openai
    from skimage.io import imread
    import numpy as np

    response = openai.Image.create(
      prompt=prompt,
      n=num_images,
      size=f"{image_size}x{image_size}"
    )
    
    images = np.asarray([imread(item['url']) for item in response['data']])
    
    if len(images) == 1:
        return images[0]
    else:
        return images
