#importing modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Controller
from time import sleep
import pyautogui

#starting interface/driver
driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe") #linking chromedriver path
driver.get("https://play.typeracer.com/") #loading site
wait = WebDriverWait(driver, 20) # defining/enabeling webdriver wait

#defining the process as a function
def process():
    
    #enabeling global variables to acess them outside the funciton
    global input1
    global text
    global ask
    global speed
    
    #selecting the racing mode on the website
    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gwt-uid-1"]/a'))).click()
    
    #reading text to type, using XPATH to locate elements
    word = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[1]'))).text
    try:
        letter2 = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[2]'))).text
    except:
        text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]'))).text
    text = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="gwt-uid-20"]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/table/tbody/tr[1]/td/div/div/span[3]'))).text
    
    #the first word is separate to the rest of the text
    text = (word,letter2,text) #joining text
    text2 = ','.join(text) #joining text
    text3  = text2.replace(',', ' ') #removing commas
    text4 = text3.replace('  ',', ') #replacing actual text commas back
    
    #deleting a space error
    index = 1 
    if len(text4) > index:
        text4 = text4[0 : index : ] + text4[index + 1 : :]
    print('Text to type: ','"',text4,'"')
    
    #sleeping - waiting for queue
    sleep(11.5)
    
    #typing with pynput library
    keyboard = Controller()
    for char in text4:
        keyboard.press(char)
        keyboard.release(char)
        sleep(speed) #waiting a certain time between typing characters - to not type too fast
    
    #function to refresh and restart another race
    print('')
    ask = input('Type 1 to do it again and bypass bot message: ')
    if ask == '1':
        driver.refresh()
        process()
    if ask != '1':
        print('See you')
        driver.quit()

#star of the code
print('Starting...')

#defining typing speed by levels
speed = float(input('Which speed? [1-3] '))
if speed == '1':
    speed = 0.1
if speed == '2':
    speed = 0.05
if speed == '3':
    speed = 0.005 #!!! change number - may be too small and you will get banned
            
# ------------- EDIT -------------
#selecting window back - I am using a double screen so use "mouseposition.py" to replace values           
pyautogui.click(583, 36) # REPLACE VALUES !!
# ------------- EDIT -------------

#starting process
process()
