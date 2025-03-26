def isPrime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

n = int(input())

for _ in range(n):
    num = int(input())
    n1 = num // 2
    n2 = num - n1
    for _ in range(n1):
        if isPrime(n1)and isPrime(n2):
            print(n1,n2)
            break
        else:
            n1 -= 1
            n2 += 1