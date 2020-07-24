from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def createMobileDriverConnection():
    baseUrl = 'http://localhost:4723/wd/hub'
    desired_caps = {
    "platformName": "Android",
    "platformVersion": "9.0",
    "deviceName": "emulator-5554",
    "automationName": "Appium",
    "app": "/Users/pulseengineering/Downloads/Sample Android Login.apk"
    }
    return webdriver.Remote(baseUrl, desired_caps)

def verifyLogin(driver, emailAddr = "", password = ""):
    emailElemId = "com.loginmodule.learning:id/textInputEditTextEmail"
    passElemId = "com.loginmodule.learning:id/textInputEditTextPassword"
    buttonLoginId = "com.loginmodule.learning:id/appCompatButtonLogin"

    if emailAddr is not "":
        element = driver.find_element_by_id(emailElemId)
        element.send_keys(emailAddr)
        assert element.text == emailAddr

    if password is not "":
        element = driver.find_element_by_id(passElemId)
        element.send_keys(password)

    element = driver.find_element_by_id(buttonLoginId)
    element.click()

if __name__ == "__main__":
    remoteDriver = createMobileDriverConnection()

    #wrong email format
    verifyLogin(remoteDriver, "test.pulse20201+1@gmail.c*&*m", "wrongPass")
    el = remoteDriver.find_element_by_link_text("Enter Valid Email")
    assert el is not None, "there must be an error : Enter valid email" 
    el =None

    #empty password
    verifyLogin(remoteDriver, "test.pulse20201+1@gmail.com", "")
    el = remoteDriver.find_element_by_link_text("Enter Valid Email")
    assert el is not None, "there must be an error : Enter valid email" 
    el =None

    #un-registered email
    verifyLogin(remoteDriver, "hazain.ahady@gmail.com", "password09!")
    el = remoteDriver.find_element_by_link_text("Wrong Email or Password")
    assert el is not None, "there must be an error : Wrong Email or Password"
    el =None
    
    #consider as positive case
    verifyLogin(remoteDriver, "test.pulse20201+1@gmail.com", "password09!")
    