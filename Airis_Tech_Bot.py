import os
import random
import time
import traceback
from threading import Timer

import chromedriver_binary
from dotenv import load_dotenv
from pushbullet import Pushbullet
from selenium import webdriver as wd
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select, WebDriverWait

load_dotenv()
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.

pb = Pushbullet('o.WbZBGDdGdZagX82oLtB2Ei3YmFzQzmsx')

website_product_not_available = "https://airistechshop.com/products/headbanger-dab-coil?_pos=2&_sid=a658e6223&_ss=r"
website_product_available = "https://airistechshop.com/collections/promote/products/airis-janus-vaporizer"

wd = wd.Chrome()


def open_webpage():
    wd.implicitly_wait(10)
    wd.get(website_product_available)


open_webpage()


def push_message(title, message):
    push = pb.push_note(title, message)


size = "W 10.5 / M 9"


def check_exists_by_xpath(xpath):
    try:
        return wd.find_element_by_xpath(xpath)
    except Exception as e:
        push_message("Airis: Element was not able to be found", xpath)
        return False
    return True


def get_env_variable(var):
    return os.environ.get(var)


def find_element_by_text(string):
    return wd.find_element_by_xpath(str('//*[text()="{}"]'.format(string)))


def find_element_by_xpath(string):
    return wd.find_element_by_xpath(str(string))


def random_time():
    random_wait_time = random.randrange(5.0, 15.0)
    print(random_wait_time)
    # time.sleep(random_wait_time)


def checkout_function():

    random_time()

    buy_now = check_exists_by_xpath(
        '//*[@id="AddToCartForm-2242892890169"]/div[3]/div/div/div/div/button[1]')
    buy_now.click()
    random_time()

    first_name_data = get_env_variable("first_name")
    last_name_data = get_env_variable("last_name")
    street_address_data = get_env_variable("street_address")
    city_data = get_env_variable("city")
    State_data = get_env_variable("state")
    zip_code_data = get_env_variable("zip_code")
    phone_number_data = get_env_variable("phone_number")
    email_data = get_env_variable("email")

    random_time()
    first_name_field = check_exists_by_xpath(
        '//*[@id="checkout_shipping_address_first_name"]')
    type(first_name_field)
    first_name_field.send_keys(first_name_data)

    random_time()
    last_name_field = check_exists_by_xpath(
        '//*[@id="checkout_shipping_address_last_name"]')
    type(last_name_field)
    last_name_field.send_keys(last_name_data)

    random_time()
    street_address_field = check_exists_by_xpath(
        '//*[@id="checkout_shipping_address_address1"]')
    type(street_address_field)
    street_address_field.send_keys(street_address_data)

    random_time()
    city_field = check_exists_by_xpath(
        '//*[@id="checkout_shipping_address_city"]')
    type(city_field)
    city_field.send_keys(city_data)

    random_time()
    zipcode_field = check_exists_by_xpath(
        '//*[@id="checkout_shipping_address_zip"]')
    type(zipcode_field)
    zipcode_field.send_keys(zip_code_data)

    random_time()
    phone_field = check_exists_by_xpath(
        '//*[@id="checkout_shipping_address_phone"]')
    type(phone_field)
    phone_field.send_keys(phone_number_data)

    random_time()
    email_field = check_exists_by_xpath('//*[@id="checkout_email"]')
    type(email_field)
    email_field.send_keys(email_data)

    random_time()
    state_field = find_element_by_xpath(
        '//*[@id="checkout_shipping_address_province"]')
    Select(state_field).select_by_value('CO')

    random_time()
    continue_shopping = check_exists_by_xpath('//*[@id="continue_button"]')
    continue_shopping.click()

    random_time()
    continue_payment = check_exists_by_xpath('//*[@id="continue_button"]')
    continue_payment.click()

    random_time()
    use_same_address = check_exists_by_xpath(
        '/html/body/div/div/div/main/div[1]/div/form/div[2]/div[2]/fieldset/div[1]')
    use_same_address.click()

    random_time()
    complete_order = check_exists_by_xpath('//*[@id="continue_button"]')
    complete_order.click()

    def input_credit_info():
        WebDriverWait(wd, 20).until(EC.frame_to_be_available_and_switch_to_it(
            (By.XPATH, '//*[@id="win-cc-pay-frame"]')))
        cc_num = check_exists_by_xpath('//*[@id="cc-number"]')
        MM_YY = check_exists_by_xpath('//*[@id="cc-exp"]')
        CVC = check_exists_by_xpath('//*[@id="cc-cvc"]')
        type(cc_num)
        cc_num.send_keys('2234')
        cc_num.send_keys('2234')
        cc_num.send_keys('2234')
        cc_num.send_keys('2234')
        type(MM_YY)
        MM_YY.send_keys(12)
        MM_YY.send_keys(52)
        type(CVC)
        CVC.send_keys(CVC_CODE)
    input_credit_info()


i_am_21 = check_exists_by_xpath(
    '//*[@id="agp_row"]/div/div/div[4]/div/form[1]/input')
i_am_21.click()


def check_for_cart_button():
    global checkout_button_exists
    checkout_button_exists = check_exists_by_xpath(
        '//*[@id="AddToCart-2242892890169"]')
    print(checkout_button_exists)
    if not checkout_button_exists:
        wd.refresh()
        Timer(5, check_for_cart_button).start()
        print('refreshed')

    else:
        push_message("Your Airis 8 tips",
                     "Your airis 8 tips are available your heinous")
        checkout_function()


try:
    check_for_cart_button()
except Exception as e:
    push_message("Airis:Main Function couldnt be started", '{}'.format(e))
    print('{}'.format(e))
