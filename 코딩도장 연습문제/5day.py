def unit19(n):
    oddList = list(range(1, 2*n, 2))
    for i in range(n):
        for k in range(n-i):
            print(' ',end='')
        for j in range(oddList[i]):
            print('*', end='')
        print()


def unit20(n1, n2):
    for i in range(n1,n2+1):
        if i%5==0 and i%7==0:
            print('FizzBuzz')
        elif i%7==0:
            print('Buzz')
        elif i%5==0:
            print('Fizz')
        else:
            print(i)
