def is_prime(potentially_prime):
    for i in range(2, potentially_prime // 2 + 1):
        if potentially_prime % 2 == 0:
            return False
    return True


primes = []

for number in range(2, 25):
    if is_prime(number):
        primes.append(number)
print(primes)

# list comprehension
_primes = [number for number in range(2, 25) if is_prime(number)]
print(_primesx)
