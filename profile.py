# this script is here to demo profiling with PyCharm


def factorialOne(n):
    i   f n == 0:
        return 1
    else:
        return n * factorialOne(n - 1)



def factorialTwo(n):
    if n == 0:
        return 1
    else:
        return n * factorialTwo(n - 1)


def doubleSqrt(n):
    return math.sqrt(math.sqrt(n))


def main():
    for x in range(0, 80000):
        resultOne = factorialOne(x)
        print(resultOne)
        resultTwo = factorialTwo(x)
        print(resultTwo)


if __name__ == "__main__":
    main()
