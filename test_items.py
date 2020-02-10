#запускать - pytest --language=es test_items.py

import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add(browser):
    browser.get(link)
    time.sleep(30)
    answer_text_elt = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    answer_text = answer_text_elt.text
    assert answer_text != 0, print("error of items")
    time.sleep(5)
