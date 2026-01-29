import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range (2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
        
    return True


num = int(input('Enter a number: '))
if is_prime(num) == True:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# version 2 -> optimized for large numbers
# this handels 2 & 3 as special cases and skips all even numbers

def is_prime_optimized(n):
    if n <= 1: return False
    if n <= 3: return True
    if n % 2 == 0 or n % 3 == 0: return False 
    
    # Check patterns of 6k +/- 1
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
        
    return True
