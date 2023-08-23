import random

num = random.randint(20, 50)
print(f'추출된 난수 : {num}')

print('<start>')
for i in range(1, num+1):
    n1 = i % 10
    n10 = i // 10

    print(f'{i:<3}', end='') # 3자리 공간을 만들고 왼쪽 정렬
    if not n1:
        print('뽀'*n10, '숑', end='', sep='')
    if n1 in [3, 6, 9]:
        print('짝', end='')
    if n10 in [3, 6, 9]:
        print('짝', end='')
    print()
