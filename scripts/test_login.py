import os, sys

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By

sys.path.append(os.getcwd())
from time import sleep
import allure
from base.base_driver import init_driver
from page.page_login import PageLogin
from base.base_yml import yml_data_with_filename_and_key
import pytest
def by_file_tars(key):
    return yml_data_with_filename_and_key("login_data",key)

class TestLogin:
    def setup(self):
        self.driver = init_driver()
        self.pagelogin = PageLogin(self.driver)
    # @pytest.mark.parametrize(("args"),by_file_tars("test_login"))
    @allure.step("步骤1")
    @pytest.mark.parametrize(("args"), by_file_tars("test_login"))
    def test_login(self,args):#,user,password
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        screen = args["screenshot"]
        allure.attach("输入用户名:"+ username )
        self.pagelogin.input_user(username)
        self.pagelogin.input_password(password)
        self.pagelogin.click_agree()
        self.pagelogin.click_login()
        ret = self.pagelogin.is_toast_exist(toast, True, screen)
        allure.attach(open('./screenshot/' + screen + '.png','rb').read(), 'tupian',allure.attachment_type.PNG)
        assert ret