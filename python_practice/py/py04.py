# 9강 실습 3
# num1 = int(input("정수를 입력하시오(1): "))
# num2 = int(input("정수를 입력하시오(2): "))
# num3 = int(input("정수를 입력하시오(3): "))
# num4 = int(input("정수를 입력하시오(4): "))
# num5 = int(input("정수를 입력하시오(5): "))
# 
# num_arr = (num1, num2, num3, num4, num5)
# 
# print('가장 큰 값 = ', max(num_arr))

n = int(input('정수를 입력하시오: '))
max = n

loop_count = 1
while loop_count <= 4 :
    n = int(input('정수를 입력하시오: '))
    if n > max :
        max = n
    loop_count += 1
print()
print('가장 큰 값 = ', max)