## 예외처리
1. try, except 문
```python
try ~ except
```

예제
```python
>>> a = 1
>>> try:
       a = int(input("please input number"))
    except ValueError:
       print("only number")
```

2. 여러개의 예외처리하기
```python
>>> a = 1
>>> try:
       ...
    except :
       ...
    except :
       ...
```

3. finally 구문  
finally 절은 try의 결과와 상관없이 무조건 실행된다
