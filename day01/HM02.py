def is_integer(value):
    return value.isdigit() or (value[0] == '-' and value[1:].isdigit())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

data_list = input("데이터를 입력하세요 (빈 칸으로 구분): ").split()

integer_values = []
prime_values = []
total_sum = 0

for data in data_list:
    if is_integer(data):
        value = int(data)
        integer_values.append(value)
        total_sum += value
        if is_prime(value):
            prime_values.append(value)

print("정수인 데이터 목록:", integer_values)
print("정수 합계:", total_sum)
print("소수인 정수 목록:", prime_values)
