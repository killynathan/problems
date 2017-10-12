# Find the sum of all the multiples of 3 or 5 below 1000.

import time

def findSumOfMultiples(threshold, *nums):
    sum = 0
    for i in range(threshold):
        for j in nums:
            if i % j == 0:
                sum += i
                break
    return sum

if __name__ == '__main__':
    start_time = time.time()
    print(findSumOfMultiples(1000, 3, 5))
    print('--- %s seconds ---' % (time.time() - start_time))
