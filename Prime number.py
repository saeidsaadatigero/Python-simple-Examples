def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

num = int(input("لطفا یک عدد وارد کنید: "))

if is_prime(num):
    print("عدد وارد شده اول است.")
else:
    print("عدد وارد شده مرکب است.")
