# 가장 큰수와 가장 작은 수를 구하는 내장 함수
data = [10, 40, 20, 70, 50, 60, 30, 50]

# sortData = sorted(data)
# maxi = sortData[-1]
# mini = sortData[0]

print(f'가장큰수 :  {max(data)}, 가장 작은수 : {min(data)}')
print(f'총합 : {sum(data)}')


# 1 ~ 10 사이의 정수 10개를 원소로 가지는 리스트 data 선언

# data = list()
# for i in range(10):
#     data.append(i+1)
# print(data)

data = [i+1 for i in range(10)]
print(data)

# 홀수만 출력해주는 방법
data = [i for i in range(10) if (i+1) % 2]
print(data)

data = [2*i+1 for i in range(5)]
print(data)

# 구구단 데이터 생성
guguData = [dan*i for dan in range(2, 10) for i in range(1, 10)]
print(guguData)

# 길이가 5인 단어 출력
strData = ['hello', 'good', 'bye', 'welcome', 'apple', 'sorry']
fiveStrData = [s for s in strData if len(s) == 5]
print(fiveStrData)

# deep copy 방법
copyStrData = strData[:]
copyStrData2 = strData.copy()

print('strData : ', strData, id(strData))
print('copyStrData : ', copyStrData, id(copyStrData))
print('copyStrData2 : ', copyStrData2, id(copyStrData2))

