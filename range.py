#نشان دادن اعداد اول بین 1 تا 100
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

primes = [num for num in range(1, 101) if is_prime(num)]
print(primes)
