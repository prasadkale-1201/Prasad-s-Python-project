for i in range (1, 101):
    count = 0
    for j in range(1, i + 1):
        if (i % j == 0):
            count += 1
    if (count == 2):
        print('Prime')
    elif i % 3 == 0 and i % 5 == 0:
     print('FizzBuzz')
    elif i % 5 == 0:
     print('Buzz')
    elif i % 3 == 0:
     print('Fizz')
    else:
     print(i)


