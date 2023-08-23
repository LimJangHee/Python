"""
    정수 2개 입력 받아 사칙 연산의 결과 출력
"""

print('첫번째 정수를 입력 : ', end='')
"""
    타입이 동적 으로 할당 되기 때문에 변수 앞에 타입을 선언 해줄 필요가 없음
    아래의 경우 str 타입을 자동 으로 할당 하는데 그래서 int type 으로 변환을 해줄 필요가 있음
"""
num01 = int(input())
# print(type(num01))
print('두번째 정수를 입력 : ', end='')
num02 = int(input())

# 출력 하는 값 사이를 특정 값으로 구분 해주고 싶을때 sep 사용
# print(num01, num02, sep=":")

print(num01, '+', num02, '=', num01 + num02)
# 값을 출력해 줄때는 밑의 방법을 더 많이 사용함
print('%d - %d = %d' % (num01, num02, num01 - num02))
print('%d * %d = %d' % (num01, num02, num01 * num02))
# Python 에서는 나누기 할때 int type 으로 나눠도 알아서 형 변환을 해서 결과 출력을 해줌(소수점 값까지 출력)
print('%d / %d = %f' % (num01, num02, num01 / num02))
# 밑의 format 방법을 사용 하면 index 를 지정 해주고 알아서 형 할당을 해줌
print('{0} / {1} = {2}'.format(num01, num02, num01 / num02))
# 밑의 방법을 사용 하면 형 할당을 알아서 해줌 다만 변수 할당을 할때 형 지정은 해줘야 함(str -> int)
print(f'{num01} / {num02} = {num01 / num02}')
# 몫만 나오게 하는 방법 (//)
print(f'{num01} / {num02} = {num01 // num02}')
# 나머지 나오게 하는 방법 (%)
print(f'{num01} % {num02} = {num01 % num02}')
# 2^3
print(2 ** 3)
print(f'{num01} ** {num02} = {num01 ** num02}')
