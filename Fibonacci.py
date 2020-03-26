def fib(n):
    if (n == 0) :
        return 0
    elif (n == 1) :
         return 1
    else :
         return (fib(n-2) + fib(n-1))

    return sum

i = 0
total = 20

while i <= total :
    print(fib(i))
    i += 1