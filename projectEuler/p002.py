# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def findFibonacciSum(threshold):
    num1 = 1
    num2 = 2
    sum = 0

    while num2 <= threshold:
        if num2 % 2 == 0:
            sum += num2
        temp = num1
        num1 = num2
        num2 = temp + num2

    return sum

if __name__ == '__main__':
    print(findFibonacciSum(4000000))
