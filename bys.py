import sys, os, time

from bs4 import BeautifulSoup
from selenium import webdriver

BYS_LOGIN = "https://bys.marmara.edu.tr/v2/Account/Login"
SUNULAN_DERSLER = "http://bys.marmara.edu.tr/ogrenci/ogr0202/default.aspx?lang=tr-TR"
DELAY = 2

def main(username, password):
    print("username: " + username)
    print("password: " + password)

    path = os.getcwd() + '/' + "chromedriver"
    driver = webdriver.Chrome(executable_path=path)
    driver.get(BYS_LOGIN)

    print("Logging in...")
    login(driver, username, password)
    print("Logged in successfully!")

    print("Downloading course list...")
    download_in_excel(driver)
    print("Downloaded successfully! Check your Downloads folder.")



def login(driver, username, password):
    username_box = driver.find_element_by_id("Username")
    password_box = driver.find_element_by_id("Password")
    login_button = driver.find_element_by_id("LoginButton")

    username_box.send_keys(username)
    password_box.send_keys(password)
    login_button.click()

    time.sleep(DELAY) # otherwise it does not get to Sunulan Dersler

def download_in_excel(driver):
    driver.get(SUNULAN_DERSLER)

    ustbirim = driver.find_element_by_name("org1$_cmbUstBirim")
    ustbirim.click()

    time.sleep(DELAY)
    muhendislik_fakultesi = driver.find_element_by_xpath("//*[ text() = 'Mühendislik Fakültesi' ]")
    muhendislik_fakultesi.click()

    time.sleep(DELAY)
    format = driver.find_element_by_name("RptExport1$cmbExport")
    format.click()
    
    time.sleep(DELAY)
    excel = driver.find_element_by_xpath("//*[ text() = 'Excel' ]")
    excel.click()

    time.sleep(DELAY)
    download = driver.find_element_by_name("RptExport1$btnExportTo")
    download.click()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid Input\nUsage: python bys.py username password")
        exit(-1)
    main(username=sys.argv[1], password=sys.argv[2])
    exit(0)
