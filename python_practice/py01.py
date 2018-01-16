level = 2
while level <= 9 :
    number = 1
    while number <= 9 :
        print(level, '*', number, ' = ', level * number)
        number+=1
    level+=1
    print()