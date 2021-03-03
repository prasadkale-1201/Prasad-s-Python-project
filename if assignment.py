def numbers(a,b,c):
    if a==b or a==c:
        Output=True
        print(Output)
    elif b==a or b==c:
        Output=True
        print(Output)
    elif c==a or c==b:
        Output = True
        print(Output)
    else:
        Output = False
        print(Output)

    return
number1 = (int(input('Please enter number1 : ')))
number2 = (int(input('Please enter number2 : ')))
number3 = (int(input('Please enter number3 : ')))
output = numbers(number1, number2, number3)
