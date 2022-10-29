

from bs4 import BeautifulSoup
# import lxml
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.support.ui import wedDriverWait
from selenium.common.exceptions import TimeoutException
import requests

import pandas as pd
from random import randint
import time 
import sys



# Add additional options to the webdriver.
firefox_options = webdriver.FirefoxOptions()
# Add the argument and make the browser Headless.
firefox_options.headless = True
# Instantiate the webdriver
driver = webdriver.Firefox(options=firefox_options, executable_path='/home/elon_musk/selenium-firefox/drivers/geckodriver')

driver.get("https://vwartclub.com/?section=studios&profile=oficina3d-brazil")
# time.sleep(5)

studio_title = driver.find_elements(By.XPATH, "/html/body/div[9]/div/div/div[1]/div[3]/div[2]/h1")
studio_country = driver.find_elements(By.CLASS_NAME, "subtitle")
studio_city = driver.find_elements(By.CLASS_NAME, "overtitle")

websites = driver.find_elements(By.XPATH, "/html/body/div[9]/div/div/div[1]/div[5]/div[1]/a")


emails = driver.find_elements(By.XPATH, "/html/body/div[9]/div/div/div[1]/div[5]/div[2]/a")
socail_media_behance = driver.find_elements(By.CSS_SELECTOR, "#column_left > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(1)")
socail_media_facebook = driver.find_elements(By.CSS_SELECTOR, "#column_left > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(2)")
socail_media_instagram = driver.find_elements(By.CSS_SELECTOR, "#column_left > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(3)")
socail_media_youtube = driver.find_elements(By.CSS_SELECTOR, "#column_left > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(4)")
socail_media_vimeo = driver.find_elements(By.CSS_SELECTOR, "#column_left > div:nth-child(3) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > a:nth-child(5)")

# related_project_number = driver.find_elements()


print([
    "Studio Title: ", studio_title[0].text,
    "/n",
    "Country: ", studio_country[0].text,
    "City: ", studio_city[0].text,
    # "Website: ", website_link[0].text,
    # "Email: ", email[0].text, 
    "Behance: ", socail_media_behance[0].text,
    "Facebook: ", socail_media_facebook[0].text,
    "Instagram: ", socail_media_instagram[0].text,
    "Youtube: ", socail_media_youtube[0].text,
    "Vimeo: ", socail_media_vimeo[0].text,
    # "Related Project Number: ", related_project_number
    ])	

for website in websites:
    herf_website = website.get_attribute('href')
    if herf_website is not None:
        print("website: ", herf_website)
    else: 
        print("No link found !!!")

for email in emails:
    herf_email = email.get_attribute('herf')
    if herf_email is not None:
        print("email: ", herf_email)
    else:
        print("no email Found !!!")

driver.quit()



# from bs4 import BeautifulSoup
# # import lxml
# from selenium import webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.firefox.options import Options
# # from selenium.webdriver.support.ui import wedDriverWait
# from selenium.common.exceptions import TimeoutException
# import requests

# import pandas as pd
# from random import randint
# import time 
# import sys


# def configure_driver():
# 	# Add additional options to the webdriver.
# 	firefox_options = webdriver.FirefoxOptions()
# 	# Add the argument and make the browser Headless.
# 	firefox_options.headless = False
# 	# Instantiate the webdriver
# 	driver = webdriver.Firefox(options=firefox_options, executable_path='/home/elon_musk/selenium-firefox/drivers/geckodriver')

# 	return driver


# def getInfo(driver):

# 	r = requests.get("https://vwartclub.com/?section=studios&profile=oficina3d-brazil")

# 	# wait for the element to laod
# 	try:
# 		soup = 	BeautifulSoup(r.text, "lxml")

# 		for studio in studio_page.select():
# 			studio_name = "div.overtitle h1"
# 			country = ""
# 			city = ""
# 			socail_media = ""
# 			email = ""
# 			website_link = ""
# 			related_project_number = ""

# 			# print scraped data
# 			print({
# 				"Studio Name: ": studio.select_one(studio_name).text,
# 				# "Country: ": ,
# 				# "City: ": ,
# 				# "socail_media: ": ,
# 				# "email: ": ,
# 				# "website_link: ": ,
# 				# "related_project_number: ": , 
# 				})



# 	except TimeoutException:
# 		print("TimeoutException: Element not found")


# driver = configure_driver()
# # studio_nam = ""
# getInfo(driver)
# driver.close()
