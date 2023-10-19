# galarina
[![License](https://img.shields.io/pypi/l/galarina.svg?color=green)](https://github.com/haesleinhuepf/galarina/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/galarina.svg?color=green)](https://pypi.org/project/galarina)
[![Python Version](https://img.shields.io/pypi/pyversions/galarina.svg?color=green)](https://python.org)
[![tests](https://github.com/haesleinhuepf/galarina/workflows/tests/badge.svg)](https://github.com/haesleinhuepf/galarina/actions)
[![codecov](https://codecov.io/gh/haesleinhuepf/galarina/branch/master/graph/badge.svg)](https://codecov.io/gh/haesleinhuepf/galarina)
[![Development Status](https://img.shields.io/pypi/status/galarina.svg)](https://en.wikipedia.org/wiki/Software_release_life_cycle#Alpha)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/galarina)](https://napari-hub.org/plugins/galarina)

A simple to use image generator based on OpenAIs DALL-E. It comes as [Juypter](https://jupyter.org/) magic, [napari](https://napari.org/) plugin and has a Python interface.

## Usage

### From Python

You can generate images from Python like this ([See example noteboo](demo/demo_galarina.ipynb)).

```
from galarina import galarina

import stackview # for visualization purposes only
```

### In Jupyter

You can use the `%gala` magic to produce a single image.

```
from galarina import gala
```

```
%gala an image of a cat
```

![docs/images/jupyter_screenshot.png]

You can also use the `%%gala` magic to produce multiple images. Just specify the number behind.

```
%%gala 3
image of cat
```

![docs/images/jupyter_screencast.gif]

### In Napari

To generate images in Napari, click the `Tools > Generate > Image` button

![docs/images/napari_screenshot.png]

## Installation

```
pip install galarina
```

If you want to use it from napari, please also install the [tools menu](https://github.com/haesleinhuepf/napari-tools-menu):

```
pip install napari-tools-menu
```

## Feedback welcome!

The napari-assistant is developed in the open because we believe in the open source community. Feel free to drop feedback as [github issue](https://github.com/haesleinhuepf/galarina) or via [image.sc](https://image.sc)

## Contributing

Contributions are very welcome. 

## License

Distributed under the terms of the [BSD-3] license,
"galarina" is free and open source software

[BSD-3]: http://opensource.org/licenses/BSD-3-Clause

