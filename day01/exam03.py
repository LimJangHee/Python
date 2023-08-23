# 논리값(True, False)
print(True, False)
print(10 > 3)
print(10 == 3)
print(10 != 3)
print("Hello" == "Hello")
print("Hello" == "hello")
print(1 == 1.0) # 값을 비교 할때 -> True
print(1 is 1.0) # 타입 까지 비교 할때 -> False, id값 즉 메모리 까지 비교 하기 때문
# id : 실제 메모리 어디에 저장이 되어 있나
print(id('Hello'))
print(id('hello'))
print(id(1))
print(id(1.0))

print("abc" and "def") # 앞이 참이면 뒤에가 출력
print("abc" or "def") # 앞이 참이면 앞이 출력

"""
    시퀀스 자료형
    list : [10, 20, 30]
    tuple : (10, 20, 30), 읽기 전용
    문자열 : 코드 사이에 ''' 사용하면 문자열로 인식
    range : 숫자 범위사이의 나열
"""

