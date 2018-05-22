def fibo(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)


def main():
    import sys
    month = int(sys.argv[1])
    print("After {} months, there are {} pairs of rabbits".format(month,
                                                                  fibo(month)))


if __name__ == "__main__":
    main()
