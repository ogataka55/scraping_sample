import time
# noinspection PyUnresolvedReferences
import chromedriver_binary
from selenium import webdriver


def main():
    food = 'トマト'
    # ドライバーの立ち上げ
    driver = webdriver.Chrome()
    # Googleにアクセス
    driver.get('https://google.com/')

    time.sleep(10)
    driver.close()


if __name__ == '__main__':
    main()
