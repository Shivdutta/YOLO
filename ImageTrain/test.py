# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 08:44:27 2020

@author: shivd
"""

from selenium import webdriver
import os
import ast
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup

driver = webdriver.Chrome("chromedriver.exe")