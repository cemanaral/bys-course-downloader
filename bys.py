import sys, os

from bs4 import BeautifulSoup
from selenium import webdriver

BYS_LOGIN = "https://bys.marmara.edu.tr/v2/Account/Login"

def main(username, password):
    print("username: " + username)
    print("password: " + password)

    path = os.getcwd() + '/' + "chromedriver"
    driver = webdriver.Chrome(executable_path=path)
    driver.get(BYS_LOGIN)
    input()

    exit(0)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Invalid Input\nUsage: python bys.py username password")
        exit(-1)

    main(username=sys.argv[1], password=sys.argv[2])
