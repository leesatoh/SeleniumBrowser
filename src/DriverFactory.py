# 必ずwithを使って、終了処理をするようにする
# WebDriverの違いの吸収を行う
import requests
from selenium.webdriver.chrome.options import Options
from MyChrome import MyChrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from requests.exceptions import Timeout


class DriverFactory(object):
    myChrome = None
    options = Options()
    port = None
    driver = None

    def __init__(self, port):
        self.port = port
        self.options.debugger_address = f"127.0.0.1:{self.port}"
        self.myChrome = MyChrome(self.port)

    def __enter__(self):
        self.myChrome.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.close()
        self.myChrome.stop()

    # ドライバーを作ります
    def get_driver(self):
        try:
            self.wait_for_port_access()
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.options)
        except Timeout:
            pass
        return self.driver

    # Chromeにアクセスできるようになるまで待ちます
    def wait_for_port_access(self):
        print("wait...chrome starting.")
        try:
            url = f'http://localhost:{self.port}/'
            requests.get(url, timeout=60)
            # TODO:リクエストのチェックもありといいか
        except Timeout:
            print("Timeout! chrome not start.")
            pass
