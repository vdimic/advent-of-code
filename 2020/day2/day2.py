#!/usr/bin/env python3
import itertools

if __name__ == '__main__':
    with open('day2.txt', 'r') as f:
        lines = f.readlines()
        valid_pass_count_part1 = 0
        valid_pass_count_part2 = 0
        for line in lines:
            policy, password = line.split(':')
            password = password.strip()
            minmax, character = policy.split()
            min, max = minmax.split('-')
            min = int(min)
            max = int(max)
            print(f'{min}|{max}|{character}|{password}')
            # Part 1
            count = 0
            for c in password:
                if c == character:
                    count +=1
            if count >= min and count <= max:
                valid_pass_count_part1 += 1
            # Part 2
            pos1_char = password[min - 1]
            pos2_char = password[max - 1]
            if pos1_char == character and pos2_char != character or pos1_char != character and pos2_char == character:
                valid_pass_count_part2 += 1

        print(valid_pass_count_part1)
        print(valid_pass_count_part2)
