# Darth-D
[![License](https://img.shields.io/pypi/l/darth-d.svg?color=green)](https://github.com/haesleinhuepf/darth-d/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/darth-d.svg?color=green)](https://pypi.org/project/darth-d)
[![Python Version](https://img.shields.io/pypi/pyversions/darth-d.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/darth-d/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/darth-d/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/darth-d/branch/master/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/darth-d)
[![Development Status](https://img.shields.io/pypi/status/darth-d.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/darth-d)](https://napari-hub.org/plugins/darth-d)

A simple to use image generator based on [OpenAIs DALL-E 2](https://openai.com/dall-e-2). 
It comes as [napari](https://napari.org/) plugin and has a Python interface. 
You need an [OpenAI API KEY](https://openai.com/blog/openai-api/) to use it.
This package allows to do some scientifically forbidden things with image data. 
Handle these functions with care.

![](https://github.com/haesleinhuepf/darth-d/raw/main/docs/images/evil_things.gif)

## Usage

### From Python

You can generate images from Python like this ([see this notebool](https://github.com/haesleinhuepf/darth-d/blob/main/demo/demo_darth-d.ipynb)).

```
from darth_d import create
```

```
image = create("an image of a cat")

image
```

![](https://github.com/haesleinhuepf/darth-d/raw/main/docs/images/jupyter_screenshot.png)

You can also vary images ([see this notebook](https://github.com/haesleinhuepf/darth-d/blob/main/demo/demo_vary.ipynb)):
```
from darth_d import vary

output_image = vary(input_image)
```

![](https://github.com/haesleinhuepf/darth-d/raw/main/docs/images/vary_screenshot.png)

Replacing regions in images is also possible. Note: handle this function with care! Do not manipulate scientific images.

![](https://github.com/haesleinhuepf/darth-d/raw/main/docs/images/jupyter_replace_screencast.gif)

### In Napari

To generate images in Napari, click the `Tools > Generate > Image` menu

![](https://github.com/haesleinhuepf/darth-d/raw/main/docs/images/napari_screenshot.png)

You can modify regions in images. Note: handle this function with care! Do not manipulate scientific images.


![](https://github.com/haesleinhuepf/darth-d/raw/main/docs/images/replace_screencast.gif)

## Installation

```
pip install darth-d
```

If you want to use it from napari, please also install the [tools menu](https://github.com/haesleinhuepf/napari-tools-menu):

```
pip install napari-tools-menu
```

## Feedback welcome!

The napari-assistant is developed in the open because we believe in the open source community. Feel free to drop feedback as [github issue](https://github.com/haesleinhuepf/darth-d) or via [image.sc](https://image.sc)

## Contributing

Contributions are very welcome. 

## License

Distributed under the terms of the [BSD-3] license,
"darth-d" is free and open source software

[BSD-3]: http://opensource.org/licenses/BSD-3-Clause

