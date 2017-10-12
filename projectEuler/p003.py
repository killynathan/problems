import math

def isPrime(num):
    if num <= 1:
        return False
    elif num <= 3:
        return True
    if (num % 2 == 0) or (num % 3 == 0):
        return False
    for i in range(5, num // 2 + 1, 2):
        if num % i == 0:
            return False
    return True

def findLargestPrimeFactor(num):
    if isPrime(num):
        return num
    for i in range(math.floor(math.sqrt(num)), 1, -1):
        if (num % i == 0) and isPrime(i):
            return i

if __name__ == '__main__':
    print(findLargestPrimeFactor(600851475143))
