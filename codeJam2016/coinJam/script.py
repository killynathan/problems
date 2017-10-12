import math

def baseConverter(binaryString, base):
    sum = 0
    for i in range(len(binaryString)):
        if binaryString[i] == '1':
            sum += math.pow(base, len(binaryString) - 1 - i)
    return sum

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

def generateJamcoins(quantity, length):
    coins = {}
    # generate coin
    # if is not prime, include in result


if __name__ == '__main__':
    print(baseConverter('1001', 9))
    
