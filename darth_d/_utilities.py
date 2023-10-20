def numpy_to_bytestream(data):
    import numpy as np
    from PIL import Image
    import io
        
    # Convert the NumPy array to a PIL Image
    image = Image.fromarray(data.astype(np.uint8)).convert("RGBA")
    
    # Create a BytesIO object
    bytes_io = io.BytesIO()
    
    # Save the PIL image to the BytesIO object as a PNG
    image.save(bytes_io, format='PNG')
    
    # To get the byte data:
    # png_image_bytes = bytes_io.getvalue()

    bytes_io.seek(0)
    return bytes_io.read()

def images_from_url_responses(response, input_shape = None):
    from skimage.io import imread
    from skimage import transform
    import numpy as np
    images = [imread(item['url']) for item in response['data']]

    if input_shape is not None:
        images = [transform.resize(image, input_shape, anti_aliasing=True, preserve_range=True).astype(image.dtype) for image in images]

        if len(input_shape) == 2 and len(images[0].shape) == 3:
            # we sent a grey-scale image and got RGB images back
            images = [image[:,:,0] for image in images]

    if len(images) == 1:
        return images[0]
    else:
        return np.asarray(images)
