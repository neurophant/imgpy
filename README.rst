ImgPy
=====

Image processing library for Python with animated GIFs support

|travisci|

.. |travisci| image:: https://travis-ci.org/embali/imgpy.svg?branch=master
    :target: https://travis-ci.org/embali/imgpy
    :alt: travis ci build status

Features
--------

* Info
* Crop
* Resize
* Thumbnail

Requirements
------------

Python 3.6+

Setup
-----

.. code-block:: bash
    
    python-3.6 -m venv .env
    source .env/bin/activate
    pip install imgpy

Usage
-----

.. code-block:: python

    from imgpy import ImgPy


    # Load target image
    im = ImgPy(fp='test.jpg')

    # Thumbnail it to 100x100 size
    im.thumbnail(size=(100, 100))

    # Save
    im.save(fp='thumb.jpg')

Tests
-----

Run tests: py.test
