def fib(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return fib(n-1)+fib(n-2)

userInput = int(input("Enter a number to input to get the Fibonacci sequence: "))
for i in range(0,userInput):
    print(fib(i))
