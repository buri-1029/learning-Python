# variable (값을 저장할 때 사용하는 식별자)
# 숫자, 문자열 등 모든 자료형을 저장 / snake_case 규칙 쓰기
a_string = "hello"
a_number = 3
a_float = 3.14
a_boolean = True    # <-> False
a_none = None       # 존재하지 않는다.
print(type(a_none))

# list (sequence & mutable)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
days.append("Sun")      # 마지막에 요소 추가
print(len(days))        # 7
print(days[0])          # Mon
print("Mon" in days)    # True
print("Man" in days)  # False

# ...
# list.reverse() - 역순
# list.remove(값) - 가장 처음 나타나는 값 삭제
# list.insert(i,값) - i번째에 값 삽입
# list.sort() - 정렬
# list.index(값) - 값의 인덱스 출력
# list.pop() - 가장 마지막 인덱스의 값 꺼내고 삭제
# list.extend([또다른리스트]) - list + 또다른리스트 확장

# tuple (sequence & immutable)
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
print(type(days))
