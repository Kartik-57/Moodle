from selenium import webdriver
from selenium.webdriver.common.keys import Keys

user = input("Enter Username/Email:  ")
pswd = input("Enter Password:  ")

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://moodle.iitd.ac.in/login/index.php")

text = driver.find_element_by_id("login").text

username = driver.find_element_by_id("username")
username.send_keys(user)

password = driver.find_element_by_id("password")
password.send_keys(pswd)

integers = []

for x in text.split():
    if x.isdigit():
        integers.append(int(x))

num = 0            
if 'first' in text:
    num = integers[0]
elif 'second' in text:
    num = integers[1]
elif 'add' in text:
    num = integers[0]+integers[1]
else:
    num = integers[0]-integers[1]

captcha = driver . find_element_by_id ("valuepkg3")
captcha.clear()
captcha.send_keys(num)

enter = driver.find_element_by_id("loginbtn")
enter.click()

