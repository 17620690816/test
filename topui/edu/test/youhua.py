import unittest
from selenium import webdriver
from  time import sleep
import time
#from public.denglu import *
dr = webdriver.Chrome()
#dr = webdriver.Firefox()
dr.maximize_window()
sleep(1)
dr.get("http://beta.bndxqc.com/index.html")#打开网站
sleep(2)
from selenium import denglu