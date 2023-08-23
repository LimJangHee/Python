data = [10, 20, 30, 40]
print(type(data), data)
data = list()
print(type(data), data)

data = (10, 20, 30, 40)
print(type(data), data)
data = tuple()
print(type(data), data)

# data = 10 int 로 인식
data = 10, 20 # 튜플로 인식함
print(type(data), data)

# range(시작=0, 종료, step=1)
data = range(10) # 10개의 숫자를 생성
print(type(data), data)
data = list(data) # 리스트로 변경해주면 0~9까지 출력
print(data)

data = range(5,15)
print(list(data)) # 5~14 까지 출력

data = list(range(1, 10, 2))
print(data)

data = list(range(20, 4, -3))
print(data)

print(16 in data, 17 in data) # 포함하고 있는지 확인
print('elo' in 'Hello')
print(10 in range(10))
