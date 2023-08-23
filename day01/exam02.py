"""
num01 = input('첫번째 정수 입력 : ')
num02 = input('두번째 정수 입력 : ')
print(num01, num02)
"""

# list type
print(type('12, 5'.split()))

# 두개의 정수를 한번에 입력 받을 때, 알아서 할당 해줌
num01, num02 = input('두개의 정수를 입력 : ').split()
# str 타입으로 할당
print(type(num01), type(num02))
# list를 split하고 각 값들의 타입을 int로 맵핑해줌
num01, num02 = map(int, input('두개의 정수를 입력 : ').split())
print(type(num01), type(num02))
