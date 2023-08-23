data = input('데이터를 입력하세요').split()
print(data)

for numStr in data:
    if numStr.isdigit():
        num = int(numStr)




num = 25
i = 2
while i < num and num % i: # 참인 경우에는 계속 돌아감 즉 나누어 떨어지면 0이라서 거짓으로 나옴
    i += 1
print('소수' if i == num else '비소수')
