from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep as wait
from selenium.webdriver.firefox.options import Options


options = Options()
options.headless = True

item = input(">> ")
driver = webdriver.Firefox(options=options)
driver.get("https://warframe.market/ru/")
print('started...')
wait(3)
search = driver.find_element(By.XPATH, '/html/body/section/section/div/section[1]/div[1]/section/div/section/div/section/span/input')
search.send_keys(item)
wait(1)
search_button = driver.find_element(By.XPATH, '/html/body/section/section/div/section[1]/div[1]/section/div/section/button')
search_button.click()
wait(3)
driver.execute_script("window.scrollTo(0, 500)") 
wait(1)
driver.save_screenshot('result.png')
driver.close()
print('===')
print('ended...')