#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time: 2021-03-07 2:15
# @Author: Yi
# @File: test_addMembers
from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
import uuid,random


class TestDemo:
    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "MI8lite"
        caps["appPackage"] = "com.tencent.wework"
        caps["appActivity"] = ".launch.LaunchSplashActivity"
        caps["noReset"] = "true"
        #如果已经安装了 io.appium.uiautomator2.server，该caps["skipServerInstallation"] = "true"可以跳过安装
        caps["skipServerInstallation"] = "true"
        caps["unicodeKeyboard"]="true"
        caps["resetKeyboard"]="true"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

        '''
        前提条件: 已登录状态（ noReset = True）
        添加通讯录用例：
        1、打开【企业微信】应用
        2、进入【通讯录】
        3、点击【添加成员】
        4、选择【手动输入添加】默认是快速添加
        5、输入【姓名:大佬】【手机:11198598511】
        6、点击【保存】
        7、检查【是否有“添加成功”提示】
        8、返回【通讯录列表查看是否有成员“大佬”】
        :return:
        '''
    @pytest.mark.parametrize("username,phone",[('大佬1'+str(uuid.uuid4())[0:3],str(11098519851+random.randint(1,9999)))])
    def test_addMemberstip(self,username,phone):
        self.driver.find_element(MobileBy.XPATH,"//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/b7m']").send_keys(username)
        self.driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.tencent.wework:id/fwi']").send_keys(phone)
        self.driver.find_element(MobileBy.XPATH,"//*[@text='保存']").click()
        #7、检查【是否有“添加成功”提示】
        self.driver.find_element(MobileBy.XPATH,'//*[@text="添加成功"]')

    @pytest.mark.parametrize("username1,phone1", [('大佬2'+str(uuid.uuid4())[:3], str(11098519851 + random.randint(1, 9999)))])
    def test_addMembersResultCheck(self,username1,phone1):
        #8、返回【通讯录列表查看是否有成员“大佬”】
        self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='添加成员']").click()
        self.driver.find_element(MobileBy.XPATH, "//*[@text='手动输入添加']").click()

        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/b7m']").send_keys(username1)
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/fwi']").send_keys(phone1)
        self.driver.find_element(MobileBy.XPATH, "//*[@text='保存']").click()
        sleep(3)
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.tencent.wework:id/ig0']").click()

        assert  username1 in  self.driver.page_source




