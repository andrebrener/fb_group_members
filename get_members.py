import os

from time import sleep

import pandas as pd

from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from constants import GROUP_MEMBERS_LINK, NUMBER_OF_SCROLLS, PASS, USER


def get_names():

    chrome_options = Options()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = Chrome(chrome_options=chrome_options)

    driver.get('https://www.facebook.com')

    sleep(2)

    username_box = driver.find_element_by_id('email')
    username_box.send_keys(USER)
    sleep(2)

    password_box = driver.find_element_by_id('pass')
    password_box.send_keys(PASS)
    sleep(1)

    login_box = driver.find_element_by_id('loginbutton')
    login_box.click()

    sleep(1)
    driver.get(GROUP_MEMBERS_LINK)

    sleep(1)

    for i in range(NUMBER_OF_SCROLLS):
        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )
        sleep(1)

    members = driver.find_elements_by_xpath(
        "//div[contains(@class, 'clearfix') and contains(@class, '_60rh')]"
    )

    names = []
    for d in members:
        link_list = d.find_elements_by_tag_name('a')
        name = link_list[1].text
        if '\n' in name:
            name = link_list[2].text

        names.append(name)

    driver.quit()

    return names


def get_group_members():
    os.makedirs('results', exist_ok=True)
    names = get_names()
    df = pd.DataFrame(names)
    df.columns = ['names']
    file_name = os.path.join('results', 'group_members.csv')
    df.drop_duplicates().to_csv(file_name, index=False)

    return None
