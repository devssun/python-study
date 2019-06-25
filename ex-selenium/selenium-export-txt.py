from bs4 import BeautifulSoup
from selenium import webdriver
import time
import sys  # sys 모듈은 파이썬 인터프리터가 제공하는 변수들과 함수들을 직접 제어할 수 있게 해주는 모듈

# 다운받은 chromedriver 의 경로를 설정한다
path = '/Users/~/chromedriver'
driver = webdriver.Chrome(path)

# 사이트 URL 로 
driver.get('https://korean.visitkorea.or.kr/main/main.html')

# 개발자 도구 (F12) 를 사용해서 검색 영역의 id를 알아온다
driver.find_element_by_id("btnSearch").click()
element = driver.find_element_by_id("inp_search")

# 이제 내일로 시즌이 오니 내일로를 검색!!
element.send_keys("내일로")

# 검색 텍스트를 클릭하면 검색이 수행된다
driver.find_element_by_link_text("검색").click()

# 검색 결과의 텍스트만 저장하기
# sys.stdout는 표준입출력을 위해 사용한다
orig_stdout = sys.stdout
f_name = '/Users/~~/output1.txt'

# 인코딩을 해야 정상적인 한글을 볼 수 있다
f = open(f_name, 'a', encoding="UTF-8")
sys.stdout = f
time.sleep(1)

# 현재 보고있는 페이지의 소스코드를 저장한다
html = driver.page_source
# html 분석
soup = BeautifulSoup(html, 'html.parser')
blog_list = soup.find('ul', class_='list_thumType flnon')

for i in blog_list:
     print(i.text.strip())
     print("\n")

sys.stdout = orig_stdout
# 파일 닫기
f.close()

# f_name 에 설정된 경로에 있는 파일을 확인해본다
