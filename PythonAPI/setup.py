from distutils.core import setup
from distutils.extension import Extension

import numpy as np
from Cython.Build import cythonize

ext_modules = [
    Extension('pycocotools._mask',
              sources=['../common/maskApi.c', 'pycocotools/_mask.pyx'],
              include_dirs=[np.get_include(), '../common'],
              extra_compile_args=[])
]

setup(name='pycocotools',
      packages=['pycocotools'],
      package_dir={'pycocotools': 'pycocotools'},
      install_requires=[
          'setuptools>=18.0', 'cython>=0.27.3', 'matplotlib>=2.1.0'
      ],
      version='2.0',
      ext_modules=cythonize(ext_modules))
