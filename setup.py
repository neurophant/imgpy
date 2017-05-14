from setuptools import setup
from codecs import open
from os import path


here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='imgpy',
    version='1.1.0',
    description='Image processing library for Python with animated GIFs support',
    long_description=long_description,
    url='https://github.com/embali/imgpy/',
    author='Anton Smolin',
    author_email='smolin.anton@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='image info crop resize thumbnail gif',
    packages=['imgpy'],
    install_requires=['Pillow>=4.1.1'],
)
