#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time: 2021-03-07 2:03
# @Author: Yi
# @File: homework1



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

    def test_demo(self):
        '''
        前提条件: 已登录状态（ noReset = True）
        打卡用例：
        1、打开【企业微信】应用
        2、进入【工作台】
        3、点击【打卡】
        4、选择【外出打卡】tab
        5、点击【第N次打卡】
        6、验证【外出打卡成功】
        7、退出【企业微信】应用
        :return:
        '''
        self.driver.find_element(MobileBy.XPATH,"//android.view.ViewGroup//*[@text='工作台']").click()
        #使用安卓自动滑到查找【打卡】
        # android_uiautomator 里面要用双引号，外面用单引号。
        # 向下滑动两次，再向上查找，直到找到元素
        self.driver.find_element(MobileBy.ANDROID_UIAUTOMATOR,
                                 'new UiScrollable(new UiSelector()'
                                 '.scrollable(true).instance(0))'
                                 '.scrollIntoView(new UiSelector()'
                                 '.text("打卡").instance(0));').click()
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡']").click()
        self.driver.find_element(MobileBy.XPATH,"//*[contains(@text,'次外出')]").click()
        #print(self.driver.page_source)
        #这样写可能会失败，因为没有等待的话，页面元素没有加载出来
        #assert '外出打卡成功' in self.driver.page_source
        #正确，应该加上显示等待或利用find_element触发隐式等待
        self.driver.find_element(MobileBy.XPATH,"//*[@text='外出打卡成功']")
