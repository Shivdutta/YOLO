# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os

folders = ['crane-operator','steel-coil','saddle','truck']
path = r'D:\YOLO\ImageTrain\collated_images'

i = 1
for folder in folders:
    for images in os.scandir(folder):
        os.rename(images.path,os.path.join(path,'{:06}.jpg'.format(i)))
        i += 1 