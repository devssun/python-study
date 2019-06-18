## python - 사용자 정의함수

1. 기본 문법
```python
def 함수이름(파라미터):
```

2. 예제
```python
>>> def plus(a, b):
       return a + b
```

3. 사용자가 여러개의 인자를 입력할 있게 하기  
파라미터 앞에 `*` 를 붙여준다
```python
def 함수이름(*파라미터):
```

4. 예제
```python
>>> def plus(*no):
       print(no)

>>> plus(1, 2, 3, 4, 5)
(1, 2, 3, 4, 5)
```

---
## python - 클래스
> class : 공용으로 쓰는 양식

```python
class 클래스이름:
```

예제
```python
>>> class sample:
       m = "a"

>>> sample = sample()

>>> sample.m
'a'
```

#### `self` 키워드
class 안에서 함수를 만들 때 변수 쓰는 자리에 반드시 self라는 키워드를 써야함
self는 class 복사 후 자체의 데이터를 활용해 함수를 실행한다



[참고자료](https://edu.goorm.io/learn/lecture/202/바로-실행해보면서-배우는-파이썬/lesson/26674/클래스-self-란)

---
## python - 모듈
> 파일로 저장하여 필요할 때 불러 사용하는 기능

