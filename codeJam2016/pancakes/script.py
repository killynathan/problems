def findMinFlips(pancakes):
    flips = 0
    for i in range(len(pancakes) - 1):
        # if i not same side as i + 1, flip all pancakes from i on up.
        if pancakes[i] != pancakes[i+1]:
            # pancakes = reverse(pancakes, i + 1)
            flips += 1

    # at last pancake, flip if necessary
    if pancakes[-1] == '-':
            flips += 1
    return flips

if __name__ == '__main__':
    fileSize = int(input())
    for i in range(fileSize):
        n = input()
        num = findMinFlips(n)
        print('Case #{0}: {1}'.format(i + 1, num))
