def find_divisors(n):
    divisors = []
    for i in range(1, n+1):
        if n%i == 0:
            divisors.append(i)
    return divisors

integer_values = []

while True:
    user_input = input("정수를 입력하세요. (끝내려면 'quit' 입력): ")
    if user_input.lower() == 'quit':
        break

    if user_input.isdigit():
        integer_values.append(int(user_input))
    else:
        print("정수를 입력하세요.")

for value in integer_values:
    divisors = find_divisors(value)
    print(f"{value}의 약수", divisors)