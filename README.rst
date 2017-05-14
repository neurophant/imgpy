ImgPy
=====

Image processing library for Python with animated GIFs support - proxy wrapper around `Pillow <https://github.com/python-pillow/Pillow/>`_ library with simple usable interface and access to each frame.

|pypi| |travisci|

.. |pypi| image:: https://badge.fury.io/py/imgpy.svg
    :target: https://badge.fury.io/py/imgpy
    :alt: pypi version
.. |travisci| image:: https://travis-ci.org/embali/imgpy.svg?branch=master
    :target: https://travis-ci.org/embali/imgpy
    :alt: travis ci build status

Features
--------

Attributes:

* `info <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.info>`_
* exif - dict with EXIF tags and GPS dict with GPS tags if presented
* `format <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.format>`_
* `size <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.size>`_
* `width <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.width>`_
* `height <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.height>`_
* `mode <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.mode>`_
* mode_desc - image mode description
* frame_count - frame count
* animated - flag, which shows if image is animated
* frames - frame list

Methods:

* `convert <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.Image.convert>`_
* `crop <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.Image.crop>`_
* `filter <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.Image.filter>`_
* `paste <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.Image.paste>`_
* `resize <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.Image.resize>`_
* `rotate <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.Image.rotate>`_
* `thumbnail <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.Image.thumbnail>`_
* `transform <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.Image.transform>`_
* `transpose <https://pillow.readthedocs.io/en/4.1.x/reference/Image.html#PIL.Image.Image.transpose>`_
* load - gets called when you access **frames** attribute for the first time or call any processing or save method, call this method explicitly to load all or limited number of frames (first n frames or random n frames without reordering)
* save - save image
* close - close image

Requirements
------------

* Python 3.5+
* Pillow 4.1.1+

Setup
-----

.. code-block:: bash
    
    python-3.6 -m venv .env
    source .env/bin/activate
    pip install imgpy

Usage
-----

.. code-block:: python

    from imgpy import Img


    # Crop image
    with Img(fp='test.gif') as im:
        im.crop(box=(10, 10, 110, 110))
        im.save(fp='crop.gif')

    # Create thumbnail image
    with Img(fp='test.gif') as im:
        im.thumbnail(size=(100, 100))
        im.save(fp='thumb.gif')

    # Save 10 random GIF frames
    with Img(fp='test.gif') as im:
        im.load(limit=10, first=False)
        im.save(fp='random.gif')

Tests
-----

Run tests: py.test
