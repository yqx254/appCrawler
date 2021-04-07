from appium import webdriver

import time


class Crawler(object):

    def __init__(self):
        self.options = {
            'platformName': "Android",
            'deviceName': "Emulator",
            'appPackage': "com.ss.android.ugc.aweme",
            'appActivity': "com.ss.android.ugc.aweme.main.MainActivity",
            "unicodeKeyboard": True,  # unicode方式发送字符串
            "resetKeyboard": True  # 隐藏软键盘
        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', self.options)

    def start(self):
        time.sleep(5)
        try:
            confirm = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/bc8")
            confirm.click()
        except:
            print("No agreement found")
        # 搜索按钮
        self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/dwo").click()
        time.sleep(3)
        # 搜索框
        edit_text = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/aia")
        edit_text.click()
        edit_text.send_keys(u"房星网")
        time.sleep(2)
        # 确定搜索
        search_res = self.driver.find_element_by_id("com.ss.android.ugc.aweme:id/kjj")
        search_res.click()
        time.sleep(5)
        # 寻找用户标签栏
        user_button = self.driver.find_elements_by_tag_name("androidx.appcompat.app.ActionBar.Tab")[2]
        user_button.click()
        time.sleep(3)
        # 点击第一个搜索结果
        dear_user = self.driver.find_elements_by_tag_name("android.widget.ImageView")[0]
        dear_user.click()
        time.sleep(5)
