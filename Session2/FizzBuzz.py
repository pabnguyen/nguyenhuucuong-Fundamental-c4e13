a = int(input("Enter: "))

if a%2 == 0 and a%3 != 0:
    print("Fizz")
elif a%3 == 0 and a%2 != 0:
    print("Buzz")
elif a%3 == 0 and a%2 == 0:
    print("FizzBuzz")
else:
    print("Ko hiện gì cả")
