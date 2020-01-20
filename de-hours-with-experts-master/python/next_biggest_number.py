#!/usr/bin/python3
import sys


def convert(list):
    res = sum(d * 10 ** i for i, d in enumerate(list[::-1]))
    return (res)

def main(digits,num):
    next_biggest_number(digits, num)


def next_biggest_number(number,num):
    orig_num=number
    n = num
    for i in range(n - 1, 0, -1):
        if number[i] > number[i - 1]:
            break

    if i == 0:
        print
        "Next number not possible"
        return

    x = number[i - 1]
    smallest = i
    for j in range(i + 1, n):
        if number[j] > x and number[j] < number[smallest]:
            smallest = j

    number[smallest], number[i - 1] = number[i - 1], number[smallest]

    x = 0
    for j in range(i):
        x = x * 10 + number[j]

    number = sorted(number[i:])
    for j in range(n - i):
        x = x * 10 + number[j]

    if x <= int(sys.argv[1]):
        x = -1
    print ("Next big number is", x)

    return x

if __name__ == "__main__":
    arg = sys.argv[1]
    digits = list(map(int,arg))
    num = len(arg)
    main(digits, num)



