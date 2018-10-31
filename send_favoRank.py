from selenium import webdriver
import datetime
import time

Date = datetime.date.today()
print(Date)
driver = webdriver.Chrome(executable_path="/Users/kudouhibiki/Desktop/python_program/chromedriver")
driver.get("https://ucblogbu.com/wp-login.php?loggedout=true")
cur_url = driver.current_url

driver.find_element_by_id('user_login').send_keys("sh05")
driver.find_element_by_id('user_pass').send_keys("roto2535")
driver.find_element_by_id('wp-submit').click()

time.sleep(3)

driver.get("https://ucblogbu.com/wp-admin/post-new.php")
driver.find_element_by_name('post_title').send_keys(str(Date.strftime("%Y年%m月%d日")) + "のバズツイートランキング")
file = open("scr_text.txt","r")
driver.find_element_by_id('content').send_keys(file.read())
driver.find_element_by_id('publish').click()
#str(date.datetime.now().strptime('%Y年%m月%日')
