## 조건문 - If
1. If 조건문 (**반드시 들여쓰기 칸을 동일하게 한다**)

```python
>>> no1 = 3

>>> if no1 == 3:
      print(no1)
      print(no1+1)
      print(no1+2)
```

2. If else 조건문
```python
>>> if money > 900:
       print('work1')
>>> else:
       print('work2')
```

3. If elif 조건문  
python에서는 elseif가 아닌 `elif` 라 작성한다
```python
>>> if url == 'www.naver.com':
        print('is naver')
>>> elif url == 'www.daum.net':
        print('is daum')
>>> else:
        print('is google')
```

4. 여러개의 조건을 동시에 체크하기
- 여러 개의 조건을 함께 만족 : `and`
- 여러 개의 조건 중 하나만 만족 : `or`
- 거짓일 때 참 : `not`
---
## 반복문 - for
> 반복 횟수 지정
1. 기본 문법
```python
for 변수 in (반복횟수):
```

2. 예제 - 문자열에서 문자 하나씩 출력하기
```python
>>> str1 = 'www.naver.com'
>>> for i in str1:
       print(i)
```

3. 범위 지정하여 반복하기 - `range()`

```python
>>> for i in range(0,10):
       print(i)
```

---
## 반복문 - while
> 조건이 틀리면 반복 종료
```python
>>> count = 1
>>> while count < 5:
       print(count)
       count += 1
```

- 건너뛰기 : `continue` 
- 반복종료 : `break`
