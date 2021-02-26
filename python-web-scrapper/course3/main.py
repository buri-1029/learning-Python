# About Django
# Django : Web Framework
# Python만 사용해서 Front End에 Back End API를 만들 수 O

# 객체지향 프로그래밍
# #1 arguments
# positional argument & keyword argument
def test(a, b, *args, **kwargs):
    print(args)     # (1, 1, 'aa', 'bb')
    print(kwargs)   # {'aa': True, 'bb': True}
    return a + b


# 무한 덧셈
def plus(*args):
    result = 0
    for num in args:
        result += num
    print(result)


test(1, 2, 1, 1, "aa", "bb", aa=True, bb=True)
plus(1, 2, 1, 2, 3, 4, 5)


# #2 class
class Car():

    # method : class안에 있는 function
    # python은 method를 호출할 때 그 method의 instance를 첫 번째 argument로 사용
    def __init__(self, *args, **kwargs):
        self.wheels = 4
        self.doors = 4
        self.windows = 4
        self.seats = 4
        self.color = kwargs.get("color", "black")
        self.price = kwargs.get("price", "$20")

    def __str__(self):
        return f"Car with {self.wheels} wheels"


# porche는 Car Class로 만든 Instance
porche = Car(color="green", price="$40")
print(porche)
print(porche.color, porche.price)   # green $40

mini = Car()
print(mini.color, mini.price)   # black $20


# #3 extend (상속) -> 확장
class Convertible(Car):

    # init method 확장
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # 부모 클래스 호출
        self.time = kwargs.get("time", 10)

    def take_off(self):
        return "take off"

    def __str__(self):
        return f"Car with no roof"


ferrari = Convertible()
print(ferrari.take_off())           # take off
print(ferrari.color, ferrari.time)  # black, 10
print(ferrari)
