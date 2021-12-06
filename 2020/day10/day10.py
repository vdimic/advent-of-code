#!/usr/bin/env python3
import time

def far(adapters, i, j):
    if abs(adapters[i] - adapters[j]) == 3:
        return True
    else:
        return False

def combination_count(group):
    combinations = {1:2,
            2:4,
            3:7,
            }
    return combinations[len(group)]

if __name__ == '__main__':
    with open('day10.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        adapters = [int(l) for l in lines]

        start_time = time.time()

        adapters.sort()
        adapters = [0] + adapters + [adapters[-1] + 3]

        jolts_diff_count = {0: 0, 1:0, 2:0, 3:0}
        for i in range(1, len(adapters)):
            jolts_diff_count[adapters[i] - adapters[i-1]] += 1
        print(jolts_diff_count)
        print(f'Final solution = {jolts_diff_count[1] * jolts_diff_count[3]}')
        print(f'Total time = {time.time() - start_time}')

        start_time = time.time()
        # List of adapter sequences that can be "played with"
        # Other adapters have to be present in the final solution
        groups = []
        current_group = []
        for i in range(1, len(adapters)-1):
            if not far(adapters, i, i-1) and not far(adapters, i, i+1):
                current_group.append(adapters[i])
            else:
                if len(current_group) > 0:
                    groups.append(current_group.copy())
                current_group = []
        print(groups)

        total_combinations = 1
        for group in groups:
            total_combinations *= combination_count(group)
        print(f'Total combinations = {total_combinations}')
        print(f'Total time = {time.time() - start_time}')
