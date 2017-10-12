import time

def isPalindrome(num):
    strNum = str(num);
    strLength = len(strNum)
    for i in range(strLength // 2):
        if strNum[i] != strNum[strLength - i - 1]:
            return False
    return True

def findLargestPalindrome():
    currentLargestPalindrome = -1
    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if product < currentLargestPalindrome:
                break
            if isPalindrome(product):
                currentLargestPalindrome = product
    return currentLargestPalindrome

if __name__ == '__main__':
    start_time = time.time()
    print(findLargestPalindrome())
    print('--- %s seconds ---' % (time.time() - start_time))
