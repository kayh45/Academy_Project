# 9강 실습 1
time = int(input("총 근무 시간을 입력하세요 : "))
pay = int(input("시간 당 급여를 입력하세요 : "))

if time > 12 :
    overTime = time - 12
    overPay = pay * 1.3 * overTime
    weekPay = pay * 12 + overPay    
else :
    weekPay = pay * time

print("총 급여는 ", int(weekPay), "원 입니다.")
