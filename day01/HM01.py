# / : float형으로,  // : 정수형으로
import random

i = random.randint(20, 50)
print('랜덤값 : ', i)

for num in range(1,i+1):
    num_str = str(num)
    output=""

    cnt = num_str.count("3") + num_str.count("6") + num_str.count('9')
    if "3" in num_str or "6" in num_str or "9" in num_str:
        if cnt == 1:
            output += "짝"
        elif cnt == 2:
            output += "짝짝"

    if num % 10 == 0:
        j = num // 10
        output += "뽀" * j + "숑"

    if output == "":
        output = num_str


    print(output)
