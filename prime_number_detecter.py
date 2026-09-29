# Problem 2: Prime Number Detector & Loop Analysis
# (Write a function is_prime(n) that accepts an integer n and returns True if n is prime, and False otherwise)
# 1. Handle edge cases ($n \le 1$ is not prime).
# 2. Optimize the loop so it only checks factors up to $\sqrt{n}$.
# 3. Write a for loop that iterates from 1 to 30 and prints all prime numbers using your function.
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
for n in range(1, 31):
    if is_prime(n):
        print(n)
