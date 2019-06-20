## Settings

1. download python 3.5.x  

2. install BeautifulSoup  
`pip3 install BeautifulSoup`  

2. install selenium  
`pip3 install selenium`  

4. selenium은 웹 브라우저를 제어해서 크롤링을 진행  
selenium이 사용할 [크롬드라이버 설치](https://sites.google.com/a/chromium.org/chromedriver/home)

---

## Selenium 으로 사이트 브라우징하기
1. setting
```python
>>> from bs4 import BeautifulSoup

# 크롬 드라이버를 사용하기 위해 import
>>> from selenium import webdriver

# sleep 을 사용하기 위해 time 모듈 import
>>> import time
```

2. 크롬드라이버 경로 설정하기
```python
>>> path = '/Users/~~~/~~~/chromedriver'
>>> driver = webdriver.Chrome(path)
>>> driver.get('https://korean.visitkorea.or.kr/main/main.html')
```

3. 검색하기 (예제 사이트 : [대한민국 구석구석](https://korean.visitkorea.or.kr/main/main.html))
```python
# element 나 id 같은 것은 F12 로 개발자 도구를 켜서 찾는다
>>> driver.find_element_by_id("btnSearch").click()
>>> element = driver.find_element_by_id("inp_search")
>>> element.send_keys("키워드")
>>> driver.find_element_by_link_text("검색").click()
```
