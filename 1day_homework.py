import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver')
driver.get("https://search.daum.net/search?nil_suggest=btn&w=img&DA=SBC&q=%ED%83%9C%EC%97%B0")
time.sleep(5)

req = driver.page_source

soup = BeautifulSoup(req, 'html.parser')

thumbnails = soup.select('#imgList > div > a > img')

i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img, f'imgs_homework/{i}.jpg')
    i += 1

driver.quit()