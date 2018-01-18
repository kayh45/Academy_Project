'''
Created on 2018. 1. 17.

@author: HNU
'''

endNum = int(input('0이상의 자연수를 입력하세요: '))
res = ()
sumAll = int()

loop = 1
while loop <= endNum :
    if loop == endNum :
        print(loop, end = '')
    else :
        print(loop, ' + ', end = '')
    sumAll += loop
    loop += 1
print(" = ", sumAll)

