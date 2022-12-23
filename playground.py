
# *args 인수로 입력되는 인수의 총합을 반환하는 로직
def add(*args):
    # print(args[0]) == 5

    result = 0
    for n in args:
        result += n
    return result


sample = add(5, 4, 3, 2, 1, 11, 10, 20)
print(sample)


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs:
    #   print(key)
    #   print(value)
    n += kwargs["add"]  # 2 + 3 =5
    n *= kwargs["multiply"]  # 5*5 = 25
    print(n)  # 25

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")  # get()함수는 딕셔너리의 Key 값으로 value를 찾는데 key가 존재하지 않아도 에러가 나지안흥ㅁ
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.sheets = kw.get("sheets")


my_car = Car(make="nissan", model="GT_R")
print(my_car.model)
