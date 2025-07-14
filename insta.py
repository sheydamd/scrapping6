import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.ChromiumEdge()
driver.get("https://www.instagram.com/")
button=driver.find_elements(By.CLASS_NAME,"_a9--")
button[0].click()
btn=driver.find_elements(By.CLASS_NAME,"_aa4b")
btn[0].send_keys("shey.damd")
btn[1].send_keys("0010101sh")
btn1=driver.find_elements(By.TAG_NAME,"form")
btn=btn1[0].find_elements(By.TAG_NAME,"button")
btn[1].click()
btn2=driver.find_elements(By.CLASS_NAME,"x78zum5")
time.sleep(100)

