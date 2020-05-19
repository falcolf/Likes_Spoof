from selenium import webdriver
from bs4 import BeautifulSoup
import time

for i in range(5):
    driver = webdriver.Chrome('./chromedriver')
    driver.get('https://kakshaa.com/themodernschool-ecncr/userWork/?userID=UserID-c4a27Ad4-5d06-4917-1d5-8')
    time.sleep(10)
    driver.execute_script('document.querySelector("#likeyyy_EntraID-439a1d70-034b-4f33-d9b-8").click()')
    driver.delete_all_cookies()
    driver.close()


