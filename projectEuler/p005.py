# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def v1():
    max = 1
    for i in range(1,21):
        max *= i
    print(max)
    for i in range(21, max + 1):
        for j in range(1,21):
            if i % j != 0:
                break;
            return i

if __name__ == '__main__':
    print(v1())
