import sys, os, time

from bs4 import BeautifulSoup
from selenium import webdriver

BYS_LOGIN = "https://bys.marmara.edu.tr/v2/Account/Login"
SUNULAN_DERSLER = "http://bys.marmara.edu.tr/ogrenci/ogr0202/default.aspx?lang=tr-TR"

def main(username, password):
    print("username: " + username)
    print("password: " + password)

    path = os.getcwd() + '/' + "chromedriver"
    driver = webdriver.Chrome(executable_path=path)
    driver.get(BYS_LOGIN)

    username_box = driver.find_element_by_id("Username")
    password_box = driver.find_element_by_id("Password")
    login_button = driver.find_element_by_id("LoginButton")

    username_box.send_keys(username)
    password_box.send_keys(password)
    login_button.click()

    time.sleep(2) # otherwise it does not get to Sunulan Dersler
    driver.get(SUNULAN_DERSLER)

    input()
    exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid Input\nUsage: python bys.py username password")
        exit(-1)

    main(username=sys.argv[1], password=sys.argv[2])
