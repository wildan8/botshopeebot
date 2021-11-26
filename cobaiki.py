from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime
from selenium.webdriver.chrome.options import Options
import requests
import re
import json
import os
import sys


start_time = time.time()
# LINK = "https://shopee.co.id/Kabel-Charger-Type-C-Aukey-Cable-CB-CD5-1M-Braided-USB-2.0-500287-i.25309502.1346196081"

LINK = "https://shopee.co.id/VYATTA-Fitme-Young-Smartwatch-Large-1.54inch-Screen-Bluetooth-Phone-Call-Multi-Style-Ui-i.109623996.10038007945"
MODEL_PROD = "Black"
INIT_HARGA = 1000
REQ = requests.Session()
# INIT SELENIUM

DRIVER_PATH = "C:\\Users\\ASUS\\Documents\\backupHTDOCS\\Tutorial\\my-project\\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(
    "user-data-dir=C:\\Users\\ASUS\\AppData\\Local\\Google\\Chrome\\User Data")
options.add_argument(f"profile-directory=default")
options.add_argument('log-level=3')

delay = 4
now = datetime.now()
current_time = now.strftime("%H:%M:%S")


def get_produk():
    r = re.search(r"i\.(\d+)\.(\d+)", LINK)
    shop_id, item_id = r[1], r[2]
    URL = f"https://shopee.co.id/api/v4/item/get?itemid={item_id}&shopid={shop_id}"
    HEAD = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    }
    GET_DATA = REQ.get(URL, headers=HEAD)
    prod = GET_DATA.json()
    items = prod["data"]
    moprod = items["models"]
    for m in moprod:
        if m["name"] == MODEL_PROD:
            print(m)
            print(m["price"])

    print(json.dumps(prod))


def get_harga():
    final_harga = 0
    r = re.search(r"i\.(\d+)\.(\d+)", LINK)
    shop_id, item_id = r[1], r[2]
    URL = f"https://shopee.co.id/api/v4/item/get?itemid={item_id}&shopid={shop_id}"
    HEAD = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    }
    GET_DATA = REQ.get(URL, headers=HEAD)
    prod = GET_DATA.json()
    items = prod["data"]
    if MODEL_PROD != "":
        if "models" in items:
            moprod = items["models"]
            for m in moprod:
                if m["name"].lower() == MODEL_PROD.lower():
                    harga = m["price"]
                    final_harga = int(harga/100000)
    else:
        harga = items["price"]
        final_harga = int(harga/100000)
    return final_harga


def click(driver, selector):
    WebDriverWait(driver, delay).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    WebDriverWait(driver, delay).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR,  selector)))
    buy = driver.find_element_by_css_selector(selector)

    driver.execute_script("arguments[0].scrollIntoView(true)", buy)
    driver.execute_script("arguments[0].click();", buy)


def just_click(driver, selector):
    buy = driver.find_element_by_css_selector(selector)

    driver.execute_script("arguments[0].scrollIntoView(true)", buy)
    driver.execute_script("arguments[0].click();", buy)


def xclick(driver, selector, xpath):
    # WebDriverWait(driver, delay).until(
    #     EC.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    # WebDriverWait(driver, delay).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR,  selector)))
    buy = driver.find_element_by_xpath(xpath)

    driver.execute_script("arguments[0].scrollIntoView(true)", buy)
    driver.execute_script("arguments[0].click();", buy)


def beli_sekarang(driver):

    if MODEL_PROD != "":
        sel_model = '#main > div > div._193wCc > div.page-product > div > div.product-briefing.flex.card.zINA0e > div.flex.flex-auto._3-GQHh > div > div._2nr4HE > div > div.flex._3AHLrn._2XdAdB > div > div:nth-child(1) > div'
        xpath_model = f"//button[contains(text(), '{MODEL_PROD}')]"
        xclick(driver, sel_model, xpath_model)
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S:%f")
        print(f"* [{current_time}] -> Click Model")

    # click(driver, '#main > div > div._193wCc > div.page-product > div > div.product-briefing.flex.card.zINA0e > div.flex.flex-auto._3-GQHh > div > div:nth-child(5) > div > div > button.btn.btn-solid-primary.btn--l._3Kiuzg')
    just_click(driver, '#main > div > div._193wCc > div.page-product > div > div.product-briefing.flex.card.zINA0e > div.flex.flex-auto._3-GQHh > div > div:nth-child(5) > div > div > button.btn.btn-solid-primary.btn--l._3Kiuzg')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%f")
    print(f"* [{current_time}] -> Beli Sekarang...")

    click(driver, '#main > div > div:nth-child(2) > div._164M6a > div > div.container > div._2jol0L._3GVi82 > div.W2HjBQ.zzOmij > button.shopee-button-solid.shopee-button-solid--primary > span')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%f")
    print(f"* [{current_time}] -> Checkout")

    click(driver, '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.qXX2_B > div > div._1n5Ut6')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%f")
    print(f"* [{current_time}] -> Ubah Payment")

    click(driver, '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.qXX2_B > div > div.checkout-payment-method-view__current.checkout-payment-setting > div.checkout-payment-setting__payment-methods-tab > span:nth-child(3) > button')
    click(driver, '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.qXX2_B > div > div.checkout-payment-setting__payment-method-options > div:nth-child(1) > div.bank-transfer-category__body > div:nth-child(8) > div')
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S:%f")
    print(f"* [{current_time}] -> TRF LAIN...")

    # Btn BUY
    # click(driver, '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.PC1-mc > div._3swGZ9 > button')
    # print(f"* [{current_time}] -> SUKSES! Alhamdulillah!")


def main():
    driver = webdriver.Chrome(executable_path=DRIVER_PATH, options=options)
    driver.get(LINK)
    print(" ")
    while True:
        harga = get_harga()
        if harga == None or harga == 0:
            driver.quit()
            sys.exit("Harga None!!")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S:%f")
        print(f"* [{current_time}] -> {harga}", end="\r")
        if harga <= INIT_HARGA:
            break

    print(" ")
    beli_sekarang(driver)


if __name__ == '__main__':
    main()


"""
https://shopee.co.id/cart?itemKeys=4809898077.11121707671.&shopId=1596789
"""
