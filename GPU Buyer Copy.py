{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "be099320-2a55-4668-834a-65549b7ba6b9",
   "metadata": {},
   "outputs": [],
   "source": [
    "from selenium import webdriver as wd\n",
    "import chromedriver_binary\n",
    "from selenium.webdriver.common.keys import Keys\n",
    "from selenium.webdriver.support.ui import Select\n",
    "import time\n",
    "import random\n",
    "from threading import Timer\n",
    "from selenium.common.exceptions import NoSuchElementException        \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "1a1996c4-65ff-49c6-840e-1b138ea34fad",
   "metadata": {},
   "outputs": [],
   "source": [
    "wd = wd.Chrome()\n",
    "wd.implicitly_wait(10)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "1e0a7059-f8e6-444d-b444-9a2b73c4a411",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<selenium.webdriver.remote.webelement.WebElement (session=\"3330614338541bb8dee31663a5bf4dcf\", element=\"098d3305-b788-45d9-b011-7725f232394b\")>\n"
     ]
    }
   ],
   "source": [
    "wd.get(\"https://www.newegg.com/Product/ComboDealDetails?ItemList=Combo.4473819&quicklink=true\")\n",
    "print(wd.find_element_by_xpath('//*[@id=\"ProductBuy\"]/div/div[2]/button'))\n",
    "\n",
    "def random_time():\n",
    "    random_wait_time = random.randrange(5.0, 15.0)\n",
    "    print(random_wait_time)\n",
    "    time.sleep(random_wait_time)\n",
    "def checkout_function():\n",
    "    random_time()\n",
    "    add_to_cart_button = wd.find_element_by_xpath('//*[@id=\"ProductBuy\"]/div/div[2]/button')\n",
    "    add_to_cart_button.click()\n",
    "\n",
    "\n",
    "    random_time()\n",
    "    proceed_to_checkout_button = wd.find_element_by_xpath('//*[@id=\"modal-intermediary\"]/div/div/div[2]/div[2]/button[2]')\n",
    "    proceed_to_checkout_button.click()\n",
    "\n",
    "    random_time()\n",
    "    continue_as_guest =  wd.find_element_by_xpath('//*[@id=\"app\"]/div/div[2]/div[2]/div/div/div/form[2]/div[2]/div/button')\n",
    "    continue_as_guest.click()\n",
    "    \n",
    "    random_time()\n",
    "    add_new_address = wd.find_element_by_xpath('//*[@id=\"shippingItemCell\"]/div/div[2]/div[2]/div/div[2]/div[2]/div/div')\n",
    "    add_new_address .click()\n",
    "\n",
    "    random_time()\n",
    "    first_name = wd.find_element_by_xpath('//*[@id=\"app\"]/div/div/div/div/div[2]/form/div[2]/div[1]/input')\n",
    "    type(first_name)\n",
    "    first_name.send_keys(\"code\")\n",
    "\n",
    "    random_time()\n",
    "    last_name = wd.find_element_by_xpath('//*[@id=\"app\"]/div[1]/div/div/div/div[2]/form/div[2]/div[2]/input')\n",
    "    type(last_name)\n",
    "    last_name.send_keys(\"name\")\n",
    "\n",
    "    random_time()\n",
    "    address = wd.find_element_by_xpath('//*[@id=\"app\"]/div[1]/div/div/div/div[2]/form/div[2]/div[6]/input')\n",
    "    type(address)\n",
    "    address.send_keys(\"61 W. Anderson Ave.\")\n",
    "\n",
    "    random_time()\n",
    "    city = wd.find_element_by_xpath('//*[@id=\"app\"]/div/div/div/div/div[2]/form/div[2]/div[10]/input')\n",
    "    type(city)\n",
    "    city.send_keys(\"Brandon\")\n",
    "\n",
    "    random_time()\n",
    "    zipcode = wd.find_element_by_xpath('//*[@id=\"app\"]/div/div/div/div/div[2]/form/div[2]/div[12]/input')\n",
    "    type(zipcode)\n",
    "    zipcode.send_keys(\"80020\")\n",
    "\n",
    "    random_time()\n",
    "    phone = wd.find_element_by_xpath('//*[@id=\"app\"]/div/div/div/div/div[2]/form/div[2]/div[14]/input')\n",
    "    type(phone)\n",
    "    phone.send_keys(\"3132454586\")\n",
    "\n",
    "    random_time()\n",
    "    email = wd.find_element_by_xpath('//*[@id=\"app\"]/div/div/div/div/div[2]/form/div[2]/div[17]/input')\n",
    "    type(email)\n",
    "    email.send_keys(\"test@ymgail.com\")\n",
    "\n",
    "\n",
    "    random_time()\n",
    "    state = wd.find_element_by_xpath('//*[@id=\"app\"]/div[1]/div/div/div/div[2]/form/div[2]/div[11]/label[2]/select')\n",
    "    Select(state).select_by_value('CO')\n",
    "\n",
    "    random_time()\n",
    "    save = wd.find_element_by_xpath('//*[@id=\"app\"]/div/div/div/div/div[3]/button[2]')\n",
    "    save.click()\n",
    "\n",
    "    random_time()\n",
    "    time.sleep(2)\n",
    "    use_address = wd.find_element_by_xpath('//*[@id=\"app\"]/div/div/div/div/div[3]/button[1]')\n",
    "    use_address.click()\n",
    "\n",
    "    random_time()\n",
    "    continue_delivery = wd.find_element_by_xpath('//*[@id=\"shippingItemCell\"]/div/div[3]/button')\n",
    "    continue_delivery.click()\n",
    "\n",
    "    random_time()\n",
    "    continue_payment = wd.find_element_by_xpath('//*[@id=\"deliveryItemCell\"]/div/div[3]/button')\n",
    "    continue_payment.click()\n",
    "\n",
    "    wd.execute_script(\"window.scrollTo(200,document.body.scrollHeight)\")\n",
    "\n",
    "\n",
    "    random_time()\n",
    "\n",
    "\n",
    "    pay_with_credit_card = wd.find_element_by_xpath('//*[@id=\"paymentItemCell\"]/div/div[2]/div/div[2]/div[2]/div[3]/div/div')\n",
    "\n",
    "    pay_with_credit_card.click()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "8d2d78f1-6900-4bfd-ae15-95c613990247",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n",
      "True\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Exception in thread Thread-16:\n",
      "Traceback (most recent call last):\n",
      "  File \"C:\\Users\\tyriq\\anaconda3\\envs\\GPU_BUY_BOT2\\lib\\threading.py\", line 973, in _bootstrap_inner\n",
      "    self.run()\n",
      "  File \"C:\\Users\\tyriq\\anaconda3\\envs\\GPU_BUY_BOT2\\lib\\threading.py\", line 1286, in run\n",
      "    self.function(*self.args, **self.kwargs)\n",
      "  File \"C:\\Users\\tyriq\\AppData\\Local\\Temp\\ipykernel_21028\\2022117097.py\", line 12, in check_for_cart_button\n",
      "  File \"C:\\Users\\tyriq\\AppData\\Local\\Temp\\ipykernel_21028\\2022117097.py\", line 3, in check_exists_by_xpath\n",
      "  File \"C:\\Users\\tyriq\\anaconda3\\envs\\GPU_BUY_BOT2\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\", line 394, in find_element_by_xpath\n",
      "    return self.find_element(by=By.XPATH, value=xpath)\n",
      "  File \"C:\\Users\\tyriq\\anaconda3\\envs\\GPU_BUY_BOT2\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\", line 976, in find_element\n",
      "    return self.execute(Command.FIND_ELEMENT, {\n",
      "  File \"C:\\Users\\tyriq\\anaconda3\\envs\\GPU_BUY_BOT2\\lib\\site-packages\\selenium\\webdriver\\remote\\webdriver.py\", line 321, in execute\n",
      "    self.error_handler.check_response(response)\n",
      "  File \"C:\\Users\\tyriq\\anaconda3\\envs\\GPU_BUY_BOT2\\lib\\site-packages\\selenium\\webdriver\\remote\\errorhandler.py\", line 242, in check_response\n",
      "    raise exception_class(message, screen, stacktrace)\n",
      "selenium.common.exceptions.WebDriverException: Message: unknown error: cannot determine loading status\n",
      "from disconnected: Unable to receive message from renderer\n",
      "  (Session info: chrome=99.0.4844.51)\n",
      "\n"
     ]
    }
   ],
   "source": [
    "def check_exists_by_xpath(xpath):\n",
    "    try:\n",
    "        wd.find_element_by_xpath(xpath)\n",
    "    except NoSuchElementException:\n",
    "        return False\n",
    "    return True\n",
    "\n",
    "\n",
    "\n",
    "def check_for_cart_button():\n",
    "    global checkout_button_exists\n",
    "    checkout_button_exists = check_exists_by_xpath('//*[@id=\"ProductBuy\"]/div/div[2]/button')\n",
    "    print(checkout_button_exists)\n",
    "    if  checkout_button_exists:\n",
    "        wd.refresh()\n",
    "        Timer(1, check_for_cart_button).start()\n",
    "        \n",
    "    else:\n",
    "        # checkout_function()\n",
    "        print(\"1\")\n",
    "\n",
    "\n",
    "check_for_cart_button()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0abdba99-6a37-42b8-a4c6-9e32df4c5e40",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f5bff5b-2726-4a8a-b4d0-fa6911e22262",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "249f04a5-086a-4f4e-b12a-e169600b69ac",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
