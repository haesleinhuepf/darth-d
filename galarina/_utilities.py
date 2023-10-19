def numpy_to_bytestream(data):
    import numpy as np
    from PIL import Image
    import io
    from stackview._image_widget import _img_to_rgb
        
    # Convert the NumPy array to a PIL Image
    image = Image.fromarray(_img_to_rgb(data).astype(np.uint8)).convert("RGBA")
    
    # Create a BytesIO object
    bytes_io = io.BytesIO()
    
    # Save the PIL image to the BytesIO object as a PNG
    image.save(bytes_io, format='PNG')
    
    # To get the byte data:
    # png_image_bytes = bytes_io.getvalue()

    bytes_io.seek(0)
    return bytes_io.read()

def images_from_url_responses(response):
    from skimage.io import imread
    import numpy as np
    images = np.asarray([imread(item['url']) for item in response['data']])
    
    if len(images) == 1:
        return images[0]
    else:
        return images