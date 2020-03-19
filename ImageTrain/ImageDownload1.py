# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 19:46:32 2020

@author: shivd
"""
from selenium import webdriver
import os
import ast
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup

driver = webdriver.Chrome("chromedriver.exe")

#url = 'https://www.google.com/search?rlz=1C2CHZL_enIN799IN815&biw=1366&bih=657&tbm=isch&sa=1&ei=qAqWXN-BD4HHvgSGhKOABA&q=sad+people+faces&oq=sad+people+faces&gs_l=img.3..0j0i8i30l2.8855278.8866576..8867376...4.0..0.405.2885.2-5j2j2......0....1..gws-wiz-img.......0i7i30j0i7i5i30j0i8i7i30j0i67.eAaFlHk83vc'
#url = 'https://www.google.com/search?tbm=isch&sxsrf=ACYBGNSRwdt_Mp1ZYBcwWCHk287H7m7mvQ%3A1578301471389&source=hp&biw=1536&bih=754&ei=H_gSXrPZFISQ4-EPy56CmAc&q=saddle&oq=saddle&gs_l=img.3..0l10.4432.6307..6889...0.0..0.129.734.0j6......0....1..gws-wiz-img.......35i39j0i131.xexGnhY8yAg&ved=0ahUKEwjz5LCUz-7mAhUEyDgGHUuPAHMQ4dUDCAY&uact=5'
url = 'https://www.google.com/search?tbm=isch&sxsrf=ACYBGNQ_gLUHp0eHMTBkjETTIJ97Nmzr2Q%3A1578282341860&source=hp&biw=1536&bih=754&ei=Za0SXvDXMpqU4-EP-563gAY&q=steel+coil&oq=steel+&gs_l=img.3.0.35i39l2j0l3j0i131j0j0i131j0l2.2244.3988..5839...0.0..0.117.665.0j6......0....1..gws-wiz-img.FITgIH_sJcA'
#url = 'https://www.google.com/search?biw=1036&bih=674&tbm=isch&sa=1&ei=e_gSXrOgF8_erQHp9J6QAw&q=truck&oq=truck&gs_l=img.3..0i67j0l9.634071.635257..636042...0.0..0.397.1235.0j5j0j1......0....1..gws-wiz-img.......0i131.RT5gej8rDFE&ved=0ahUKEwjzyaLAz-7mAhVPbysKHWm6BzIQ4dUDCAc&uact=5'
#url  = 'https://www.google.com/search?biw=1536&bih=710&tbm=isch&sa=1&ei=VPwSXuC_JNGDrtoPyOSa0Ac&q=crane+operator&oq=crane+operator&gs_l=img.3..0i67j0l3j0i67l2j0l3j0i67.0.0..635185...2.0..0.171.306.0j2......0......gws-wiz-img.9gn_HrmKOLA&ved=0ahUKEwjguYeW0-7mAhXRgUsFHUiyBnoQ4dUDCAc&uact=5'

#directory = 'saddle'
directory = 'steel-coil'
#directory = 'truck'
#directory = 'crane-operator'

def find_urls(url):
    driver.get(url)
    wait = input('Press Enter To Save')
    page = driver.page_source

    soup = Soup(page,'lxml')
    urls = soup.find_all('div',{'class':'rg_meta notranslate'})

    all_urls = []
    for i in urls:
        link = i.text
        link = ast.literal_eval(link)['ou']
        print(link)
        all_urls.append(link)
    return all_urls

URLs = find_urls(url)

def save_img(url,directory):
    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i,link in enumerate(url):
        path = os.path.join(directory,'{:06}.jpg'.format(i))
        try:
            success=ulib.urlretrieve(link,path)
            print('Success:'+path)
        except:
            print('Failed: ' +path)

save_img(URLs,directory)