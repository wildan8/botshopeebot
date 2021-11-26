from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import re
import json
import os
import sys


class Selenlib():

    driver = ""
    delay = 4

    def __init__(self, driver_path, user_data_dir):
        self.DRIVER_PATH = driver_path
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
        self.options.add_argument(f"user-data-dir={user_data_dir}")
        self.options.add_argument("profile-directory=default")
        self.options.add_argument('log-level=3')

    def open_link(self, LINK):
        self.driver = webdriver.Chrome(
            executable_path=self.DRIVER_PATH, options=self.options)
        self.driver.get(LINK)

    def click(self, selector):
        try:
            WebDriverWait(self.driver, self.delay).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
            WebDriverWait(self.driver, self.delay).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,  selector)))
            buy = self.driver.find_element_by_css_selector(selector)

            self.driver.execute_script(
                "arguments[0].scrollIntoView(true)", buy)
            self.driver.execute_script("arguments[0].click();", buy)
        except TimeoutException as ex:
            print(f"* [ERROR] -> Exception has been thrown. " + str(ex))

    def just_click(self, selector):
        buy = self.driver.find_element_by_css_selector(selector)

        self.driver.execute_script("arguments[0].scrollIntoView(true)", buy)
        self.driver.execute_script("arguments[0].click();", buy)

    def xclick(self, xpath):
        buy = self.driver.find_element_by_xpath(xpath)

        if "product-variation--disabled" not in buy.get_attribute("class").split():
            self.driver.execute_script(
                "arguments[0].scrollIntoView(true)", buy)
            # self.driver.execute_script("arguments[0].click();", buy)
            buy.click()
            return True
        else:
            return False

    def beli_sekarang(self, MODEL_PROD, MODEL_ALL):
        if MODEL_PROD != "":
            sel_model = '#main > div > div._193wCc > div.page-product > div > div.product-briefing.flex.card.zINA0e > div.flex.flex-auto._3-GQHh > div > div._2nr4HE > div > div.flex._3AHLrn._2XdAdB > div > div:nth-child(1) > div'
            xpath_model = f"//button[contains(text(), '{MODEL_PROD}')]"
            clik_model = self.xclick(xpath_model)
            if clik_model == False:
                for ma in MODEL_ALL:
                    xpath_model = f"//button[contains(text(), '{ma}')]"
                    clik_model = self.xclick(xpath_model)
                    print(f"_ TRY {ma}")
                    if clik_model == True:
                        break

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S:%f")
            if clik_model == False:
                sys.exit(f"* [{current_time}] -> WES PAYUUU!!!!")
            else:
                print(f"* [{current_time}] -> Click Model")

        self.just_click('#main > div > div._193wCc > div.page-product > div > div.product-briefing.flex.card.zINA0e > div.flex.flex-auto._3-GQHh > div > div:nth-child(5) > div > div > button.btn.btn-solid-primary.btn--l._3Kiuzg')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S:%f")
        print(f"* [{current_time}] -> Beli Sekarang...")

        self.click('#main > div > div:nth-child(2) > div._164M6a > div > div.container > div._2jol0L._3GVi82 > div.W2HjBQ.zzOmij > button.shopee-button-solid.shopee-button-solid--primary > span')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S:%f")
        print(f"* [{current_time}] -> Checkout")

        self.click(
            '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.qXX2_B > div > div._1n5Ut6')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S:%f")
        print(f"* [{current_time}] -> Ubah Payment")

        self.click('#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.qXX2_B > div > div.checkout-payment-method-view__current.checkout-payment-setting > div.checkout-payment-setting__payment-methods-tab > span:nth-child(3) > button')
        self.click('#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.qXX2_B > div > div.checkout-payment-setting__payment-method-options > div:nth-child(1) > div.bank-transfer-category__body > div:nth-child(8) > div')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S:%f")
        print(f"* [{current_time}] -> TRF LAIN...")

        # Btn BUY
        # self.click('#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.PC1-mc > div._3swGZ9 > button')
        # print(f"* [{current_time}] -> SUKSES! Alhamdulillah!")
