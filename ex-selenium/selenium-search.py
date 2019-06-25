from bs4 import BeautifulSoup
from selenium import webdriver
import time

# 다운받은 chromedriver 의 경로를 설정해줍니다
path = '/Users/~/chromedriver'
driver = webdriver.Chrome(path)

# 사이트 URL 로 
driver.get('https://korean.visitkorea.or.kr/main/main.html')

# 개발자 도구 (F12) 를 사용해서 검색 영역의 id를 알아옵니다
driver.find_element_by_id("btnSearch").click()
element = driver.find_element_by_id("inp_search")

# 이제 내일로 시즌이 오니 내일로를 검색해봅니다
element.send_keys("내일로")

# 검색 텍스트를 클릭하면 검색이 수행됩니다
driver.find_element_by_link_text("검색").click()
