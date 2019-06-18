## OS 모듈
> 폴더 생성 및 이동, 삭제 시 사용

```python
>>> import os
>>> os
<module 'os' from '~~~~~~~~~3.7/lib/python3.7/os.py'>
```

- 디렉토리 이동 : `chdir()`
- 현재 작입 디렉토리 위치 가져오기 :  `getcwd()`
- 특정 디렉토리 안에 있는 목록 가져오기 : `listdir()`

- 폴더 만들기 : `mkdir()` (오류 확인 가능)
  - 하위 폴더를 여러개 만들 때 사용`makedirs()`  
    (오타가 있어도 오류를 알 수 없음)
    
- 폴더 삭제 : `rmdir()` (폴더 안에 파일이 없는 경우)
  - 폴더의 세부 내용을 함께 삭제 : `removedirs()` (강제 삭제)
  
---

## 파일 불러오기 / 저장하기
1. txt 파일로 저장하기

`open`에는 세가지 모드가 있다
- `w` : 쓰기 / 덮어쓰기
- `a` : 추가하기
- `r' : 파일 읽기

```python
# 디렉토리 이동
>>> os.chdir("python/python-study")
# 파일 열고 쓰기
>>> f = open("test.txt", "w")
>>> f.write('make new file')
13
# 파일 닫기
>>> f.close()
```

2. xls, csv 형식으로 저장하기  
**주의점 - 엑셀과 csv 형식으로 저장하기 위해 먼저 표 형식으로 데이터를 생성해야 함**  

* 관련 프로그램을 설치한다
  - numpy  
  - pandas

  ```
  1. 먼저 pip를 업그레이드한다
  pip3 install --upgrade pip

  2. python3을 사용하기 때문에 pip3 로 설치한다
  pip3 install numpy
  pip3 install pandas
  ```
  
  
