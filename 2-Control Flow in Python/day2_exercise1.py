import math


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True


if __name__ == "__main__":
    while True:
        try:
            num = int(input("Enter a number: "))
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")