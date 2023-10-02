import pytest
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import requests

with open("/Users/sona/Desktop/AutoTest_Python/lekcia&Seminar_4/testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

@pytest.fixture(scope="session")   #будет действовать всю сессию
def browser(): #эта часть инициализирует браузер
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit() #выполняем выход из драйвера

@pytest.fixture()
def login():
    response = requests.post(testdata["url_login"],
                             data={'username': testdata["login"], 'password': testdata["password"]})
    if response.status_code == 200:
        return response.json()['token']





