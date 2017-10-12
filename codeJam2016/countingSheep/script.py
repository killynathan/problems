def findLastNumberBeforeSleep(n):
    if n == 0:
        return 'INSOMNIA'
    visited = set()
    for i in range(1,1000):
        num = i * n
        # get every digit in n and add to visited
        strNum = str(num)
        for char in strNum:
            visited.add(char)

        # if visited is full, return n
        if len(visited) == 10:
            return num

if __name__ == '__main__':
    fileSize = int(input())
    for i in range(fileSize):
        n = int(input())
        num = findLastNumberBeforeSleep(n)
        print('Case #{0}: {1}'.format(i + 1, num))
