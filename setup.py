#!/usr/bin/env python

import os
import glob
from setuptools import setup, Extension

libwheel_src = glob.glob("libwheel/src/*.cpp")
libwheel_inc = ["libwheel/include"]
libwheel_libs = ["wiringPi"]
libwheel_ext = {"sources": libwheel_src, "include_dirs": libwheel_inc, "libraries": libwheel_libs}

config = {
    'name':'libwheel', 
    'version':'0.1',
    'description':'Python interface for libwheel',
    'package_dir':{'libwheel': 'libwheel/python'},
    'py_modules':['libwheel.__init__'],
    'ext_modules':[Extension("_libwheel", **libwheel_ext)],
    'scripts':[],
}

if __name__ == "__main__":
    setup(**config)


