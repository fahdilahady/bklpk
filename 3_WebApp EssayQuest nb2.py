from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
userName = "test.pulse20201@gmail.com"
passWord = "Pruservice@20"

def accessToWeb(address):
    driver.get(address)
    #driver.maximize_window()

def openLoginPage():
    element = driver.find_element_by_link_text('Login')
    element.click()
    print('open login page')
    return element

def fillLoginData(_userName, _password):
    element = driver.find_element_by_id("user_session_username") 
    element.send_keys(_userName)#user_session_username

    element = driver.find_element_by_id('user_session_password')
    element.send_keys(_password)

    element.send_keys(Keys.RETURN)
    print("execute login :",_userName, _password)
    return element

def searchAProduct(productName):
    element = driver.find_element_by_id("v-omnisearch__input")
    element.send_keys(productName)
    element.send_keys(Keys.RETURN)

if __name__ == "__main__":
    accessToWeb("https://www.bukalapak.com/")
    assert "Bukalapak" in driver.title
    driver.implicitly_wait(30)
    
    element = openLoginPage()
    assert "Bukalapak" in driver.title, "wrong web app, expected Bukalapak"
    assert "No results found." not in driver.page_source 
    

    element = fillLoginData('wrongEmailFormat@google','wrongPas')#negative case 
    #assert "Username atau password yang kamu masukkan salah" in driver.page_source , "negative case expected: wrong pass / email"

    element = fillLoginData(userName, passWord) #positive case 
    assert "flash=you_login" in driver.current_url
    print(driver.current_url)
    
    searchAProduct("Kolam Anak")
    assert "Kolam" in driver.current_url
    assert "Anak" in driver.current_url


    driver.close()
    
    
    