# 변수
first_name = 'kuemryoung'
last_name = 'kong'

print(first_name + last_name)

# 리스트
# 순서가 중요 index 0부터 시작
a_list = ['수박', '참외','배']
b_list = ['영희', '철수',['사과','감']] # list 안에 list 가능

a_list.append('수박') # 내용 추가 append

print(a_list[1])
print(b_list[2][0])

# 딕셔너리
# key - value 값을 사용 , 순서가 중요하지 않음
a_dict = {'name':'bob', 'age' :24}
a_dict['height'] = 178
a_list = ['수박', '참외','배']
a_dict['fruit'] = a_list

print(a_dict['name'])
print(a_dict['fruit'][0]) # 딕셔너리는 key 값으로 찾고, list는 숫자(index)로 찾는다.

# 조건문 - tab을 지켜주는 것이 중요 ㄴ
age = 24

if age > 20:
    print("성인입니다.")
    print("성인입니다2.")
else:
    print("청소년입니다.")

# 반복문

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for fruit in fruits:
    if fruit == '배':
        count += 1

print(count)

people = [{'name': 'bob', 'age': 20},
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7},
          {'name': 'smith', 'age': 17},
          {'name': 'ben', 'age': 27}]

for person in people:
    if person['age'] > 20:
        print(person['name'])

# 내장 함수

# 문자열 쪼개기 - split()
myemail = 'sparta@naver.com'

# result = myemail.split('@')[1].split('.')[0] # - 어느 도메인의 이메일인지 찾아보는 코드 완성

# print(result)

# 문자열 바꾸기 - replace()
result = myemail.replace('naver', 'gmail')

print(result)

# 패키지, 라이브러리
'''
python에서 패키지는 모듈(일종의 기능들 묶음)을 모아 놓은 단위이고, 이런 패키지의 
묶음을 라이브러리라고 합니다. 하지만 보통 패키지와 라이브러리는 홍요해서 많이 쓴다. 
'''

# 가상환경 - virtual enviroment - venv

# dload

import dload
dload.save("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c6/Jeju_Island.jpg/375px-Jeju_Island.jpg")

# 이미지 웹 스크래핑(크롤링)하기

# 브라우저 제어 - selenium
# 우리가 원하는 것을 취할 수 있는 라이브러리 - BeaurtifulSoup
from selenium import webdriver
driver = webdriver.Chrome('chromedriver')

driver.get("http://www.naver.com")

import dload
from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver') # 웹드라이버 파일의 경로
driver.get("https://search.daum.net/search?w=img&nil_search=btn&DA=NTB&enc=utf8&q=%EC%95%84%EC%9D%B4%EC%9C%A0")
time.sleep(5) # 5초 동안 페이지 로딩 기다리기

req = driver.page_source
# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
# soup이라는 변수에 "파싱 용이해진 html"이 담긴 상태가 됨
# 이제 코딩을 통해 필요한 부분을 추출하면 된다.
soup = BeautifulSoup(req, 'html.parser')

###################################
# 이제 여기에 코딩을 하면 됩니다!
###################################

thumbnails = soup.select('#imgList > div > a > img')

i = 1
for thumbnail in thumbnails:
    img = thumbnail['src']
    dload.save(img,f'img/{i}.jpg')
    i += 1


driver.quit() # 끝나면 닫아주기