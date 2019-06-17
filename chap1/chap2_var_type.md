### 문자
1. 배열에 문자 저장하기
```python
>>> str1 = 'python'
```

2. 인덱싱
```python
>>> str1[0]
'p'
```

3. 슬라이싱
```python
>>> str1[0:2]
'py'
>>> str1[ :2]
'py'
>>> str1[2:]
'thon'
```

4. meta-character & escape chracter
- 줄바꿈 `\n`
- tab `\t`

- 줄바꿈 적용 안하게 `\\n`

5. 문자 조작 함수
- 대문자 변환 `upper()`
- 소문자 변환 `lower()`
- 문자 변환 `replace()`
- 문자열 분리 `split()`
- 길이 확인 `len()`


---

### 리스트
1. 리스트 생성 및 초기호
```python
>>> list1 = [3, 42, 'sdf']
```

2. 리스트 데이터 추가
- 마지막에 추가 `append()`
- 원하는 위치에 추가 `insert(인덱스, 데이터)`

3. 리스트 데이터 삭제
- 리스트 항목 삭제하기 `remove()`
- 삭제할 인덱스 삭제하기 `del(인덱스)`

4. 리스트 정렬하기 - 같은 데이터형으로 이루어진 배열만 가능
- sort() / reverse()

5. 리스트 개수
```python
len(list1)
```

---
### list / tuple 의 차이
- 데이터 생성 문법 차이 (list = [] / tuple = ())

- list는 데이터 추가 및 삭제 가능
- tuple은 수정 불가

### dictionary
- 내용 수정 가능
- 데이터 값을 구분하는 키 값이 있음

**dictionary 생성하기**
```python
>>> dic1 = {'key1': 3, 'key2': 3}
```

- 모든 키 조회 - `keys()`
- 모든 값 조회 - `values()`
