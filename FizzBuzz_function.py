# Task 1: FizzBuzz with a Twist
# [Write a program that loops through numbers from 1 to 50]:

# 1. For multiples of 3, print "Fizz".

# 2. For multiples of 5, print "Buzz".

# 3. For numbers that are multiples of both 3 and 5, print "FizzBuzz".

# 4. For prime numbers, print "Prime". (Note: If a prime number is also a multiple of 3 or 5—like 3 or 5—prioritize printing "Prime").

# 5. For all other numbers, print the number itself.
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    limit = int(n ** 0.5)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True

for num in range(1, 51):
    if is_prime(num):
        print("Prime")
    elif num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
