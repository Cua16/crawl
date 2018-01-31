# coding=utf-8
import pdfkit
import requests
import re
from bs4 import BeautifulSoup
import os
import os.path
import re
import time
import logging
from save_as_pdf import save_pdf
from os_test import send_email
url_main='https://www.liaoxuefeng.com'
url='https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
def get_urls(url,data=None):
    wb_data=requests.get(url,headers=headers)
    time.sleep(3)
    soup=BeautifulSoup(wb_data.text,'lxml')
    hrefs=soup.select('[class="x-wiki-index-item"]')
    #WritingPattern=re.compile('')
    for href in hrefs:
        data=str(url_main+href.get('href'))
        html=url+data
        #print(data)
        name=r'E:\python_example\pdf_files'+'\\'+data[-7:-3]
        #print(name)
        save_pdf.save_pdf_note(data,name+'.pdf')
get_urls(url)

