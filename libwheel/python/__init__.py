import os
import itertools
from ctypes import cdll

def load_library(libname):
    mod_path = os.path.split(__file__)[0]
    search_path = os.path.join(mod_path, "..", ".")
    for (root, dirs, files) in os.walk(search_path):
        for fn in files:
            if fn.lower().startswith(libname) and fn.lower().endswith(".so"):
                libpath = os.path.join(root, fn)
                return cdll.LoadLibrary(libpath)
    return cdll.LoadLibrary(libname)

# load our library
libname = "_libwheel"

class Wheel(object):
    LibraryName = "_libwheel"
    _wheel = None

    @property
    def wheel(self):
        if self.__class__._wheel == None:
            self.__class__._wheel = load_library(libname)
        return self.__class__._wheel

    def __init__(self, bind):
        self.obj = bind

    def startWheel(self):
        self.wheel.startWheel(self.obj)

    def getWheelRate(self):
        return self.wheel.getWheelRate(self.obj)

    def getWheelQueueSize(self):
        return self.wheel.getWheelQueueSize()

    def pushWheelKeys(self, pKey1, pKey2):
        self.wheel.getWheelQueueSize(self.obj, pKey1, pKey2)
