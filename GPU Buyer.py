#!/usr/bin/env python
# coding: utf-8

# In[21]:


from selenium import webdriver as wd
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
import random
from threading import Timer
from selenium.common.exceptions import NoSuchElementException        


# In[22]:


wd = wd.Chrome()
wd.implicitly_wait(10)


# In[23]:


wd.get("https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4473819&quicklink=true")
print(wd.find_element_by_xpath('//*[@id="ProductBuy"]/div/div[2]/button'))

def random_time():
    random_wait_time = random.randrange(5.0, 15.0)
    print(random_wait_time)
    time.sleep(random_wait_time)
def checkout_function():
    random_time()
    add_to_cart_button = wd.find_element_by_xpath('//*[@id="ProductBuy"]/div/div[2]/button')
    add_to_cart_button.click()


    random_time()
    proceed_to_checkout_button = wd.find_element_by_xpath('//*[@id="modal-intermediary"]/div/div/div[2]/div[2]/button[2]')
    proceed_to_checkout_button.click()

    random_time()
    continue_as_guest =  wd.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div/div/div/form[2]/div[2]/div/button')
    continue_as_guest.click()
    
    random_time()
    add_new_address = wd.find_element_by_xpath('//*[@id="shippingItemCell"]/div/div[2]/div[2]/div/div[2]/div[2]/div/div')
    add_new_address .click()

    random_time()
    first_name = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[1]/input')
    type(first_name)
    first_name.send_keys("code")

    random_time()
    last_name = wd.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/form/div[2]/div[2]/input')
    type(last_name)
    last_name.send_keys("name")

    random_time()
    address = wd.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/form/div[2]/div[6]/input')
    type(address)
    address.send_keys("61 W. Anderson Ave.")

    random_time()
    city = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[10]/input')
    type(city)
    city.send_keys("Brandon")

    random_time()
    zipcode = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[12]/input')
    type(zipcode)
    zipcode.send_keys("80020")

    random_time()
    phone = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[14]/input')
    type(phone)
    phone.send_keys("3132454586")

    random_time()
    email = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[2]/form/div[2]/div[17]/input')
    type(email)
    email.send_keys("test@ymgail.com")


    random_time()
    state = wd.find_element_by_xpath('//*[@id="app"]/div[1]/div/div/div/div[2]/form/div[2]/div[11]/label[2]/select')
    Select(state).select_by_value('CO')

    random_time()
    save = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/button[2]')
    save.click()

    random_time()
    time.sleep(2)
    use_address = wd.find_element_by_xpath('//*[@id="app"]/div/div/div/div/div[3]/button[1]')
    use_address.click()

    random_time()
    continue_delivery = wd.find_element_by_xpath('//*[@id="shippingItemCell"]/div/div[3]/button')
    continue_delivery.click()

    random_time()
    continue_payment = wd.find_element_by_xpath('//*[@id="deliveryItemCell"]/div/div[3]/button')
    continue_payment.click()

    wd.execute_script("window.scrollTo(200,document.body.scrollHeight)")


    random_time()


    pay_with_credit_card = wd.find_element_by_xpath('//*[@id="paymentItemCell"]/div/div[2]/div/div[2]/div[2]/div[3]/div/div')

    pay_with_credit_card.click()


# In[24]:


def check_exists_by_xpath(xpath):
    try:
        wd.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True



def check_for_cart_button():
    global checkout_button_exists
    checkout_button_exists = check_exists_by_xpath('//*[@id="ProductBuy"]/div/div[2]/button')
    print(checkout_button_exists)
    if  checkout_button_exists:
        wd.refresh()
        Timer(1, check_for_cart_button).start()
        
    else:
        # checkout_function()
        print("1")


check_for_cart_button()


# In[ ]:





# In[ ]:





# In[ ]:




