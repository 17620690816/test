#coding=utf-8
import os
import unittest
from appium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

desired_caps = {
                'platformName': 'Android',        # 声明是ios还是Android系统
                'deviceName': 'H6QSOZROWKDYIJ8L',   # 连接的设备名称
                'automationName': 'Appium',         #用哪种自动化引擎。appium（默认）还是Selendroid
                'platformVersion': '7.1.1',        # Android系统版本号，可以在夜神模拟器设置或手机中查看
                'appPackage': 'com.bonade.xxp.test', #应用包名字
                'appActivity':'com.bonade.xxp.ui.splash.SplashActivity' #测试app的Activity名字
                }

driver = webdriver.Remote('http://192.168.0.64:4723/wd/hub', desired_caps) #启动APP
time.sleep(5)
driver.find_element_by_id("com.bonade.xxp.test:id/goto_settings").click()#点击下一步
time.sleep(1)
driver.find_element_by_id("com.android.packageinstaller:id/do_not_ask_checkbox").click()#勾选不再询问
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()#始终允许
time.sleep(1)
driver.find_element_by_id("com.android.packageinstaller:id/do_not_ask_checkbox").click()#勾选不再询问
driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()#始终允许
time.sleep(7)
driver.find_element_by_class_name("android.widget.TextView").click()#跳过
time.sleep(3)
driver.find_element_by_class_name("android.widget.ImageView").click()#关闭公告
'''
#APP与H5切换
#打印出当前手机页面的context
contexts = driver.contexts
print(contexts)

# 切换到webview
driver.switch_to.context("NATIVE_APP")

# 获取当前的环境，看是否切换成功
now = driver.current_context
print(now)

# 切回native
driver.switch_to.context(contexts[0])
# driver.switch_to.context("NATIVE_APP") # 这样也是可以的

# 获取当前的环境，看是否切换成功
now = driver.current_context
print (now)
'''
driver.implicitly_wait(10)
driver.find_element_by_xpath("//android.widget.LinearLayout[@resource-id='com.bonade.xxp.test:id/layout_approve']").click()
#el = driver.find_element_by_android_uiautomator(id).click()#审批
time.sleep(3)
driver.find_element_by_id("com.bonade.xxp.test:id/tv_nologin_head_portrait").click()#登录按钮
time.sleep(2)
driver.find_element_by_id("com.bonade.xxp.test:id/et").send_keys("17620690816")#账号
time.sleep(1)
driver.find_element_by_id("com.bonade.xxp.test:id/et").send_keys("111111")#密码
time.sleep(1)
driver.find_element_by_id("com.bonade.xxp.test:id/login_button").click()#登录
time.sleep(1)

driver.find_element_by_id("com.android.calculator2:id/digit7").click()
driver.find_element_by_id("com.android.calculator2:id/plus").click()
driver.find_element_by_id("com.android.calculator2:id/digit3").click()
driver.find_element_by_id("com.android.calculator2:id/equal").click()
time.sleep(5)
'''
driver.find_element_by_class_name("android.support.v7.widget.RecyclerView")
driver.find_element_by_id("com.bonade.xxp.test:id/layout_approve").click()
time.sleep(3)
'''