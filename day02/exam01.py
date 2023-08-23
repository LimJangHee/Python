"""
    list 내장함수
    append : 데이터 추가(맨 마지막)
    insert : 데이터 추가(특정 위치에)
    pop    : 데이터 삭제(맨 마지막)
    remove : 데이터 삭제(특정 데이터)
    index  : 특정값의 위치 검색
    count  : 특정값의 빈도수
    reverse: 위치 뒤집기
    sort   : 정렬
    clear  : 리스트 요소 전부 삭제
"""

data = []
print(data, id(data))
data.append(10)
data.append(20)
data.append(30)
print(data, id(data))
delData = data.pop()
print('삭제된 값 : ', delData)

data = list()
# 0번지에 차례대로 들어가기 때문에 앞에 넣었던 값들은 뒤로 밀림
data.insert(0, 10)
data.insert(0, 20)
data.insert(0, 30)
print(data, id(data))
delData = data.pop()
print('삭제된 값 : ', delData)

data = []
data.append(10)
data.append(20)
data.append(30)
print(data, id(data))
delData = data.pop(0) # index 사용 가능
print('삭제된 값 : ', delData)

data = [10, 20, 30, 40]
idx = data.index(30)
cnt = data.count(30)
print('위치 : ', idx)
print('개수 : ', cnt)
print('before : ', data)
data.remove(30)
print('after : ', data)

for i in range(len(data)):
    print(data[i], end='')
print()

for d in data:
    print(d, end='')
print()

# 이터레이터, next로 계속 변경해줘야 함
# ite = iter(data)
# print(next(ite))
# print(next(ite))
# print(next(ite))
# print(next(ite))

for d in iter(data):
    print(d, end='')
print()

data.reverse() # 배열 역순으로 다시 배열해주는 함수
for d in iter(data):
    print(d, end='')
print()
data.reverse() # 원상 복귀 할려면 다시 reverse해줘야 함

data2 = reversed(data) # 원본 배열은 그대로 두고 새롭고 대입하는 대상 배열에만 역순으로 넣어줌
print('data : ', data)
print('data2 : ', next(data2))

for d in reversed(data):
    print(d, end='')
print()

# data.sort() # 숫자의 경우 오름차순으로 정렬해줌
# print(data)
print(sorted(data, reverse=True)) # 원본 배열은 그대로 두고 정렬 해줌(true설정을 해줘서 내림차순으로 정렬해줌)
print(data)

data = [10, 20, 30]
# for i in range(len(data)):
#     data.pop(0)
# data.clear()
del data[:]
print(data)

for i in range(1, len(data)+1):
    print(data[-i], end='')
print()

# 인덱스 출력용 내장함수(enumerate)
for index, d in enumerate(data, start=1): # 인덱스와 해당 값을 동시에 접근, start를 통해서 시작 인덱스를 지정해줄 수 있음
    print(f'[{index}] : {d}')
print()

