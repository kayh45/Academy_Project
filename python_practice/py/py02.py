# 9강 실습 2
num = int(input("양의 정수를 입력하세요 : "))

print(num, '의 약수  = ', end = '')

loop = 1
count = 0
while loop <= num :
     if (num%loop == 0) :
         print(loop, end = ' ')
         count += 1
     loop+=1

print()
print('약수의 개수 = ', count)