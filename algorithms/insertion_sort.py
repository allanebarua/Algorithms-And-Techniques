"""Insertion sort algorithm."""
import sys


def do_insertion_sort(numbers):
    """Sort list in place using insertion sort."""
    for i in range(1, len(numbers)):
        j = i - 1
        while j >= 0:
            if numbers[j] <= numbers[j + 1]:
                break

            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp
            j -= 1


if __name__ == '__main__':
    numbers = [
        number
        for number in map(int, sys.argv[1].split(','))
    ]
    do_insertion_sort(numbers)
    print(numbers)
