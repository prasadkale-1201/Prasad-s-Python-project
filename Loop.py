def board(row,column):
    row = int(input('Please enter odd row numbers : '))
    column = int(input('Please enter odd column numbers : '))
    for num in range(row):
        if num%2 == 0:
            for num1 in range(1,column+1):
                if num1%2 ==1:
                   if num1 != column:
                    print(" ", end="")
                   else:
                    print(" ")
                else:
                     print("|", end="")
        else:
             print("-"*column)
    output = True
    print(output)
    return
TicTac = board(7,7)
