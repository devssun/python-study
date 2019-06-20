## BeautifulSoup 사용하기

install
```
pip3 install beautifulsoup4
```

1. crawling/분석 할 html 문서 가져오기
```python
# bs 모듈 import
>>> from bs4 import BeautifulSoup
# 임시 html 포맷 저장
>>> html = """
... <html>
...     <head>
...             <title>html practice </title>
...     </head>
...     <body>
...             <p align="center"> text content </p>
...     </body>
... </html> """
>>>
```

2. BeautifulSoup 분석
```python
>>> bs = BeautifulSoup(html, 'html.parser')
```
3. 태그 찾기 - `find()`
```python
# find() 는 조건에 맞는 분석 결과가 여러개 있어도 첫번 째만 return 한다
# 구분하기 위해 속성 값을 준다
>>> bs.find('title')
<title>html practice </title>

>>> bs.find("p", align="center")
<p align="center"> text content </p>
```

4. 태그 찾기2 - find_all()  
조건에 맞는 태그를 모두 가져올 때 사용
```python
>>> bs.find_all('title')

# 정규식과 결합하여 사용할 수 있다
>>> tags = bs.find_all(re.compile("^p"))
```

---

5. 태그 골라내기 - `select()`
[실습 파일](chap1/practice_bs_fruits.html)

```python
# 태그명
>>> soup.select('span')
  
# 클래스
>>> soup.select('.price')
  
# 하위태그
# 하위태그를 가져올 때는 반드시 '>' 양쪽에 공백을 줘야한다
>>> soup.select('상위태그 > 하위태그 > 하위태그' )

# [0], [1] ... 을 줘서 원하는 순서의 값만 가져올 수 있다
>>> soup.select('상위태그 > 하위태그 > 하위태그' )[0]

# 특정 태그의 특정 클래스 가져오기
>>> soup.select('상위태그.클래스이름 > 하위태그.클래스이름')

# 특정 아이디 가져오기
>>> soup.select('#아이디')
```




