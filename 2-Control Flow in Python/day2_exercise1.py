import math

while True:
    try:
        num = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter an integer.")

if num > 1:
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")