num=1
while num <= 10:
    print(num, end='')
    num += 1

# for 변수 in range()
for i in range(1,11):
    print(i, end='')

# 범위 내 홀수 출력
for i in range(0, 10, 2):
    print(i+1, end='')
print()

names = ['홍길동', ' 강길동', '윤길동']
for name in names:
    print(name, end='')
print()

for i in range(0, 6, 1):
    print('*' * i)

for i in range(5):
    print('*' * (i+1))

for i in range(9):
    if i < 5:
        print('*' * (i+1))
    else:
        print('*' * (9-i))

for i in range(9):
    # 참문장 if 조건식 else 거짓문장
    cnt = (i+1) if i < 5 else (9-i)
    print('*' * cnt)