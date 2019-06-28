# setting
from bs4 import BeautifulSoup
from selenium import webdriver
import time

# path
path = '~~/chromedriver'
driver = webdriver.Chrome(path)

# 24 시간 운영하는 매장만 검색합니다
driver.get('http://www.hollys.co.kr/store/korea/korStore.do?pageNo=1&sido=&gugun=&store=&allday=1')

# 현재 조회된 소스 저장
source = driver.page_source

# parser
soup = BeautifulSoup(source, 'html.parser')

# 카페 이름과 주소 가져오기 - TODO: 함수로 만들기
result = []
tags = soup.select('td > a')
for tag in tags:
    result.append(tag.text)

# 분리하여 저장하기 - TODO: 함수로 만들기
titles = []
address = []
for i in range(0, len(result)):
    if i % 2 == 0:
        titles.append(result[i])
    else:
        address.append(result[i])

# 다음 페이지로 이동하기
element = driver.find_element_by_class_name("paging")
element.find_element_by_link_text("2").click()

# 자동화
# TODO 1: 현재 페이지 번호 가져오기
# TODO 2: 현재 보고있는 페이지에서 html parser 실행하기
# TODO 3: table 코드 파싱하기
# TODO 4: 상점 이름과 주소만 가져오기
# TODO 5: 다음 페이지가 있는 지 확인하기
# TODO 6: 있으면 이동하기 - 2번부터 반복
# TODO 7: 없으면 종료하기
