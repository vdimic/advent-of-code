#!/usr/bin/env python3
import time


if __name__ == '__main__':
    with open('day15.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        nums = [int(n) for n in lines[0].split(',')]
        print(nums)
        #Part 1
        turn = 1
        last_spoken = {}
        lastlast_spoken = {}
        last_spoken_num = None

        for n in nums:
            last_spoken[n] = turn
            last_spoken_num = n
            turn += 1
        print(last_spoken_num)
        while turn <= 30000000:
            if turn % 100000 == 0:
                print(f'turn {turn}')
            #print(f'turn:{turn} last_spoken_num:{last_spoken_num} history:{last_spoken}')
            if last_spoken_num in last_spoken and last_spoken_num in lastlast_spoken:
                new_num = last_spoken[last_spoken_num] - lastlast_spoken[last_spoken_num]
            else:
                new_num = 0
            #print(f'speak:{new_num}')
            if new_num in last_spoken:
                lastlast_spoken[new_num] = last_spoken[new_num]
            last_spoken[new_num] = turn
            last_spoken_num = new_num
            turn += 1


        start_time = time.time()
        print(f'Final solution part 1 = {last_spoken_num}')
        print(f'Total time = {time.time() - start_time}')

