# if a number is divisible by 3 print Fizz
# if a number is divisible by 5 print Buzz
# if a number is divisible by both 3 and 5 print Fizz Buzz
# otherwise print the number

r = int(input("Enter a range for Fizz Buzz: "))


def fizz_buzz(r):
    for i in range(1, r+1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 5 == 0:
            print("Buzz")
        elif i % 3 == 0:
            print("Fizz")
        else:
            print(i)


fizz_buzz(r)
