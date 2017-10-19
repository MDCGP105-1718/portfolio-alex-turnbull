def fizzBuzz(low,high):
    for i in range(low,high):
        if i%3 == 0 and i%5 == 0:
            print(str(i) +": FizzBuzz")
        elif i%5 == 0:
            print(str(i) + ": Buzz")
        elif i%3 == 0:
            print(str(i) + ": Fizz")
        else:
            print(i)


fizzBuzz(int(input("low number")),int(input("high number")))

