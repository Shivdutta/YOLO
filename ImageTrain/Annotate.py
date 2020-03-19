# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:25:07 2020

@author: shivd
"""

import os
import matplotlib.pyplot as plt
import cv2
from matplotlib.widgets import RectangleSelector
from matplotlib.widgets import TextBox

# global constants
img = None
tl_list = []
br_list = []
object_list = []
#textValue = None

# constants
image_folder = 'collated_images'
savedir = 'annotations'
obj = 'a'

from lxml import etree
import xml.etree.cElementTree as ET


def write_xml(folder, img, objects, tl, br, savedir, textValue):
    if not os.path.isdir(savedir):
        os.mkdir(savedir)

    image = cv2.imread(img.path)
    height, width, depth = image.shape

    annotation = ET.Element('annotation')
    ET.SubElement(annotation, 'folder').text = folder
    ET.SubElement(annotation, 'filename').text = img.name
    ET.SubElement(annotation, 'segmented').text = '0'
    size = ET.SubElement(annotation, 'size')
    ET.SubElement(size, 'width').text = str(width)
    ET.SubElement(size, 'height').text = str(height)
    ET.SubElement(size, 'depth').text = str(depth)
    for obj, topl, botr in zip(objects, tl, br):
        ob = ET.SubElement(annotation, 'object')
        ET.SubElement(ob, 'name').text = textValue
        ET.SubElement(ob, 'pose').text = 'Unspecified'
        ET.SubElement(ob, 'truncated').text = '0'
        ET.SubElement(ob, 'difficult').text = '0'
        bbox = ET.SubElement(ob, 'bndbox')
        ET.SubElement(bbox, 'xmin').text = str(topl[0])
        ET.SubElement(bbox, 'ymin').text = str(topl[1])
        ET.SubElement(bbox, 'xmax').text = str(botr[0])
        ET.SubElement(bbox, 'ymax').text = str(botr[1])

    xml_str = ET.tostring(annotation)
    root = etree.fromstring(xml_str)
    xml_str = etree.tostring(root, pretty_print=True)
    # print(xml_str)
    save_path = os.path.join(savedir, img.name.replace('jpg', 'xml'))
    print(save_path)
    with open(save_path, 'wb') as temp_xml:
        a = temp_xml.write(xml_str)
        # print(a)


def line_select_callback(clk, rls):
    global tl_list
    global br_list
    global object_list
    tl_list.append((int(clk.xdata), int(clk.ydata)))
    br_list.append((int(rls.xdata), int(rls.ydata)))
    object_list.append(obj)


def onkeypress(event):
    global object_list
    global tl_list
    global br_list
    global img
    if event.key == 'q':
        # print(object_list)
        # print(tl_list)
        # print(br_list)
        # print(image_folder)
        # print(savedir)
        print("Text" + text_box.text)
        write_xml(image_folder, img, object_list, tl_list, br_list, savedir, text_box.text)
        tl_list = []
        br_list = []
        object_list = []
        img = None


def toggle_selector(event):
    toggle_selector.RS.set_active(True)


if __name__ == '__main__':
    for n, image_file in enumerate(os.scandir(image_folder)):
        img = image_file
        fig, ax = plt.subplots(1, figsize=(10.5, 8))
        mngr = plt.get_current_fig_manager()
        # mngr.window.setGeometry=(250, 40, 800, 600)
        image = cv2.imread(image_file.path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(image)

        # name = input("Enter a name: ")
        # print(name)
        axbox = plt.axes([0.1, 0.075, 0.8, 0.095])
        text_box = TextBox(axbox, '', initial='')
        #print(("Text" + text_box.text))
        #textValue = text_box.text

        toggle_selector.RS = RectangleSelector(
            ax, line_select_callback,
            drawtype='box', useblit=True,
            button=[1], minspanx=5, minspany=5,
            spancoords='pixels', interactive=True,
        )
        bbox = plt.connect('key_press_event', toggle_selector)
        key = plt.connect('key_press_event', onkeypress)
        plt.tight_layout()
        plt.show()
        plt.close(fig)
