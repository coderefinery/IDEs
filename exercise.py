HELLO_WORLD = "Hello World!"


def main():
    counter = 1

    while True:
        printer()
        counter += 1


def printer():
    print(HELLO_WORLD)


if __name__ == '__main__':
    main()
