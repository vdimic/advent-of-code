#!/usr/bin/env python3
import itertools
import time


if __name__ == '__main__':
    with open('day14.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        #Part 1
        start_time = time.time()
        mem = {}
        mem2 = {}
        addrs2 = []
        for line in lines:
            tokens = line.replace('[', ' ').replace(']', '').replace(' = ', ' ').split(' ')
            # Part 1
            if tokens[0] == 'mask':
                or_mask = int(''.join(['1' if c == '1' else '0' for c in tokens[1]]),2)
                and_mask = int(''.join(['0' if c == '0' else '1' for c in tokens[1]]),2)
            else:
                mem[tokens[1]] = int(tokens[2]) & and_mask | or_mask

            # Part 2
            if tokens[0] == 'mask':
                mask2 = tokens[1]
                or_mask = int(''.join(['1' if c == '1' else '0' for c in tokens[1]]),2)
                x_positions = [i for i in range(len(mask2)) if mask2[i] == 'X']
            else:
                addr = int(tokens[1]) | or_mask # Force ones
                # create all combinations for X-es
                curr_addr = "{0:036b}".format(addr)
                curr_addr = [c if mask2[i] != 'X' else 'X' for i, c in enumerate(curr_addr)]
                for x_vals in itertools.product(*[['0','1'] for _ in range(len(x_positions))]):
                    for i, x_pos in enumerate(x_positions):
                        curr_addr[x_pos] = x_vals[i]
                    mem2[int(''.join(curr_addr),2)] = int(tokens[2])

            print(line.count('X'))
        sum = 0
        for addr, val  in mem.items():
            sum += val
        print(f'Final solution part 1 = {sum}')

        sum = 0
        for addr, val in mem2.items():
            sum += val
        print(f'Final solution part 2 = {sum}')

        print(f'Total time = {time.time() - start_time}')

