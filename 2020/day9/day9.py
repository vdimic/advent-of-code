#!/usr/bin/env python3

def have_a_pair_sum(list, num):
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if i == j:
                continue
            if list[i] + list[j] == num:
                return True
    return False


if __name__ == '__main__':
    with open('day9.txt', 'r') as f:
        lines = [int(l.strip()) for l in f.readlines()]

        nums = []
        # Part 1
        for line in lines:
            if len(nums) == 25:
                if not have_a_pair_sum(nums, line):
                    print(line)
                    invalid_num = line
                    break
                else:
                    nums = nums[1:]
            nums.append(line)

        # Part 2
        i = 0
        chosen = []
        sum = 0
        while True:
            while sum < invalid_num:
                if i == len(lines):
                    break
                chosen.append(lines[i])
                sum += lines[i]
                i += 1
            if sum == invalid_num:
                #DONE
                print(chosen)
                print(min(chosen) + max(chosen))
                exit()

            while sum > invalid_num:
                sum -= chosen[0]
                chosen = chosen[1:]

