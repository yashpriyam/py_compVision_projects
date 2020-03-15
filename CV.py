#Module for cv2 utility functions and maintaining version compatibility
#between 3.x and 4.x
#"""
import cv2
from maskrcnn_benchmark.utils import cv2_util

def findContours(*args, **kwargs):
    #"""
    #Wraps cv2.findContours to maintain compatiblity between versions
    #3 and 4
    #Returns:
    #    contours, hierarchy
    #"""
    if cv2.__version__.startswith('4'):
        contours, hierarchy = cv2.findContours(*args, **kwargs)
    elif cv2.__version__.startswith('3'):
        _, contours, hierarchy = cv2.findContours(*args, **kwargs)
    else:
        raise AssertionError()
    return contours, hierarchy