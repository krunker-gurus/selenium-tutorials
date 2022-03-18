# importing modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Controller
from time import sleep
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service

print('''
████████╗██╗   ██╗██████╗ ███████╗██████╗  ██████╗ ████████╗
╚══██╔══╝╚██╗ ██╔╝██╔══██╗██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
   ██║    ╚████╔╝ ██████╔╝█████╗  ██████╔╝██║   ██║   ██║   
   ██║     ╚██╔╝  ██╔═══╝ ██╔══╝  ██╔══██╗██║   ██║   ██║   
   ██║      ██║   ██║     ███████╗██████╔╝╚██████╔╝   ██║   
   ╚═╝      ╚═╝   ╚═╝     ╚══════╝╚═════╝  ╚═════╝    ╚═╝   
                                                            
 Credits to htpps://github.com/xtekky ▮
 ''')

# starting interface/driver
chromedriver_autoinstaller.install()  # installing auto chromedriver
driver = webdriver.Chrome(service=Service())  # linking chromedriver to driver variable function
driver.get("https://play.typeracer.com/")  # loading site
wait = WebDriverWait(driver, 20)  # defining/enabeling webdriver wait


# defining the process as a function
def process():
    # enabeling global variables to acess them outside the funciton
    global input1
    global text
    global ask
    global speed

    # selecting the racing mode on the website
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[3]'))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gwt-uid-1"]/a'))).click()

    # reading text to type, using XPATH to locate elements
    word = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]'))).text
    try:
        letter2 = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]'))).text
    except:
        text = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]'))).text
    text = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]'))).text

    # the first word is separate to the rest of the text
    text = (word, letter2, text)  # joining text
    text2 = ','.join(text)  # joining text
    text3 = text2.replace(',', ' ')  # removing commas
    text4 = text3.replace('  ', ', ')  # replacing actual text commas back

    # deleting a space error
    index = 1
    if len(text4) > index:
        text4 = text4[0: index:] + text4[index + 1::]
    print('Text to type: ', '"', text4, '"')

    class element_has_css_class(object):

        def __init__(self, locator, css_class):
            self.locator = locator
            self.css_class = css_class

        def __call__(self, driver):
            element = driver.find_element(*self.locator)  # Finding the referenced element
            if self.css_class in element.get_attribute("class"):
                return element
            else:
                return False


    # sleeping - waiting for queue
    wait.until(element_has_css_class((By.XPATH, '/html/body/div[6]'), "gwt-PopupPanel"))

    # typing with pynput library
    keyboard = Controller()
    for char in text4:
        keyboard.press(char)
        keyboard.release(char)
        sleep(0.03)  # waiting a certain time between typing characters - to not type too fast

    # function to refresh and restart another race
    print('')
    ask = input('Type 1 to do it again and bypass bot message: ')
    if ask == '1':
        driver.refresh()
        process()
    if ask != '1':
        print('See you')
        driver.quit()


if __name__ == "__main__":
    # starting process
    print('Starting...')
    process()
