from selenium import webdriver as wd
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
from threading import Timer
from selenium.common.exceptions import NoSuchElementException
from pushbullet import Pushbullet
import traceback
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')  # Last I checked this was necessary.

pb = Pushbullet('o.WbZBGDdGdZagX82oLtB2Ei3YmFzQzmsx')

website_product_not_available = "https://airistechshop.com/products/headbanger-dab-coil?_pos=2&_sid=a658e6223&_ss=r"
website_product_available = "https://airistechshop.com/collections/promote/products/airis-janus-vaporizer"

wd = wd.Chrome(chrome_options=options)


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

    first_name = 'Tyrique'
    last_name = 'Daniel'
    street_address = '3860 red deer trail'
    city = 'broomfield'
    State = 'Co'
    zip_code = '80020'
    phone_number = '3054330078'
    email = 'Tyriquedaniel4@gmail.com'

    random_time()
    first_name = check_exists_by_xpath(
        '//*[@id="checkout_shipping_address_first_name"]')
    type(first_name)
    first_name.send_keys('Tyrique')

    random_time()
    last_name = check_exists_by_xpath(
        '//*[@id="checkout_shipping_address_last_name"]')
    type(last_name)
    last_name.send_keys('Daniel')

    random_time()
    address = check_exists_by_xpath(
        '//*[@id="checkout_shipping_address_address1"]')
    type(address)
    address.send_keys('3860 red deer trail')

    random_time()
    city = check_exists_by_xpath('//*[@id="checkout_shipping_address_city"]')
    type(city)
    city.send_keys('Broomfield')

    random_time()
    zipcode = check_exists_by_xpath('//*[@id="checkout_shipping_address_zip"]')
    type(zipcode)
    zipcode.send_keys('80020')

    random_time()
    phone = check_exists_by_xpath('//*[@id="checkout_shipping_address_phone"]')
    type(phone)
    phone.send_keys('3054330078')

    random_time()
    email = check_exists_by_xpath('//*[@id="checkout_email"]')
    type(email)
    email.send_keys('Tyriquedaniel4@gmail.com')

    random_time()
    state = find_element_by_xpath(
        '//*[@id="checkout_shipping_address_province"]')
    Select(state).select_by_value('CO')

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
