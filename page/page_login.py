import os, sys

from appium.webdriver.common.touch_action import TouchAction
from time import sleep
sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By

from base.base_action import BaseAction
class PageLogin(BaseAction):
    menu_button = By.XPATH, "text,我的"
    button_head = By.ID, "com.tpshop.malls:id/head_img"
    text_user = By.ID, "com.tpshop.malls:id/mobile_et"
    text_password = By.ID, "com.tpshop.malls:id/pwd_et"
    buttom_agree = By.XPATH, "resource-id,com.tpshop.malls:id/agree_btn"
    buttom_login = By.XPATH, "resource-id,com.tpshop.malls:id/login_tv"

    def __init__(self,driver):
        BaseAction.__init__(self,driver)
        self.click_my()
        self.click_head()
    def click_my(self):
        self.click(self.menu_button)
    def click_head(self):
        self.click(self.button_head)
    def input_user(self,text):
        self.input_text(self.text_user,text)
    def input_password(self,text):
        self.input_text(self.text_password,text)
    def click_agree(self):
        self.click(self.buttom_agree)
    def click_login(self):
        self.click(self.buttom_login)
