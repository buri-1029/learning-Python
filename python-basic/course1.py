# python basic course 1 by 'nomadcoder'
import math
import datetime
from calculator import times, division
# from math import ceil, fsum 사용할 것만 import!

# variable (값을 저장할 때 사용하는 식별자)
# 숫자, 문자열 등 모든 자료형을 저장 / snake_case 규칙 쓰기
a_string = "hello"
a_number = 3
a_float = 3.14
a_boolean = True     # <-> False
a_none = None        # 존재하지 않는다.
print(type(a_none))  # <class 'NoneType'>


# list : sequence & mutable
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
days.append("Sun")      # 마지막에 요소 추가
print(len(days))        # 7
print(days[0])          # Mon
print(days[0:2])        # ['Mon', 'Tue']
print(days[0:5:2])      # ['Mon', 'Wed', 'Fri']
print("Mon" in days)    # True
print("Man" in days)    # False

# 값 in list / 값 not in list
# len(list) : 리스트 길이
# list * 3  : 리스트 반복
# list_a + list_b : 리스트 연결
# list.append(요소) : 리스트에 요소 추가
# list.insert(인덱스, 요소) : 리스트에 요소 추가
# list.pop(인덱스) : 인덱스로 요소 제거
# list.remove(값) : 값으로 요소 제거(맨 앞쪽에 있는 것이)
# list.clear() : 모두 제거
# list.reverse() : 역순
# list.sort() : 정렬
# list.index(값) : 값의 인덱스 출력
# list_a.extend([list_b]) : 리스트 확장
# ...


# Tuples and Dicts
# tuple : sequence & immutable
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
print(type(days))  # <class 'tuple'>

# dictionary
buhee = {
    "name": "buhee",
    "age": 26,
    "korean": True,
    "fav_fruit": ["Apple", "Banana"]
}

print(buhee)
# {'name': 'buhee', 'age': 26, 'korean': True, 'fav_fruit': ['Apple', 'Banana']}
buhee["female"] = True
print(buhee)
# {'name': 'buhee', 'age': 26, 'korean': True, 'fav_fruit': ['Apple', 'Banana'], 'female': True}


# Built in Functions
age = "100"
print(len(age))     # 3
print(type(age))    # <class 'str'>
n_age = int(age)    # 타입 변환
print(type(n_age))  # <class 'int'>


# Function()
def say_hello(name='unknown'):
    print('hello ', name)


say_hello('buhee')  # hello  buhee
say_hello()         # hello  unknown


def plus(a, b):
    return a + b


print(plus(b=3, a=1))  # 4


# if elif else
# (< <= > >= == != is is not)
# (and or)
def score_check(score):
    result = ''
    if score >= 90:
        result = 'A'
    elif score >= 80:
        result = 'B'
    elif score >= 70:
        result = 'C'
    else:
        result = 'F'
    return result


print(score_check(60))  # F


# for in ** important **
for num in [1, 2, 3, 4, 5]:
    print(num)
# 1
# 2
# 3
# 4
# 5

# break, continue, pass
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

for day in days:
    if day is "Wed":
        break
    else:
        print(day)
# Mon
# Tue

for letter in "buhee":
    print(letter)
# b
# u
# h
# e
# e

# Module - math, datetime, email,,,
print(math.ceil(1.2))   # 올림    2
print(math.sqrt(9))     # 제곱근  3.0
print(math.fabs(-1.2))  # 절대값  1.2
print(datetime.datetime.now())  # 현재 날짜/시간

# 다른 파일에서 정의된 기능을 import 해서 사용 가능
#   - calculator.py import 하여 times와 division 함수 사용
print(times(3, 2), division(4, 2), "hello")
# 6 2 hello
