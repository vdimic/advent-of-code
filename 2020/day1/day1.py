#!/usr/bin/env python3
import itertools

if __name__ == '__main__':
    with open('day1.txt', 'r') as f:
        lines = f.readlines()
        numbers = [int(line) for line in lines]
        # Part 1
        for i, j in itertools.product(range(len(numbers)), range(len(numbers))):
            if i == j:
                continue
            elif numbers[i] + numbers[j] == 2020:
                print(f'{numbers[i] * numbers[j]}')
                break

        # Part 2
        for i, j, k in itertools.product(range(len(numbers)), range(len(numbers)), range(len(numbers))):
            if i == j or j == k or i == k:
                continue
            elif numbers[i] + numbers[j] + numbers[k] == 2020:
                print(f'{numbers[i] * numbers[j] * numbers[k]}')
                break
