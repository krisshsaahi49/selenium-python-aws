import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.loginpage import LoginPage
from selenium_stealth import stealth

URL = "https://automation.krisshsaahi.dev"

@pytest.fixture
def driver():
    option = webdriver.ChromeOptions()
    option.add_argument("headless")
    option.add_argument("--start-maximized")
    option.add_argument("--no-sandbox")
    option.add_argument("--disable-extensions")
    option.add_argument("--disable-gpu")
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    # service = ChromeService(executable_path="/root/chromedriver-linux64/chromedriver")
    # driver = webdriver.Chrome(service=service, options=option)
    driver = webdriver.Chrome(service=ChromeService(executable_path=ChromeDriverManager().install()), options=option)
    stealth(driver,
            languages=["en-US", "en"],
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
            )
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.implicitly_wait(15)
    yield driver
    driver.close()
    driver.quit()

@pytest.mark.parametrize("username, password", [("test","test"),("test_user1","test"),("aditya","aditya")])
def test_signin(driver, username, password):
    login = LoginPage(driver)
    login.launch(URL)
    login.enter_username(username)
    login.enter_password(password)
    login.login_title()
    print("Signin Test Complete")

def test_rentacar(driver):
    test_signin(driver,"test","test")
    from pages.homepage import HomePage
    home = HomePage(driver)
    home.goto_4runner()
    home.rent_car("Indianapolis")
    print("Rent a car Test Complete")
