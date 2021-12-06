#!/usr/bin/env python3
import time

def execute_command(cmd, val, x, y):
    print(f'{cmd} {value}')
    if cmd == 'N':
        return x, y + value
    elif cmd == 'E':
        return x + value, y
    elif cmd == 'S':
        return x, y - value
    elif cmd == 'W':
        return x - value, y
    else:
        print("FAIL")
        exit()

dir_to_cmd = {0: 'N',
        90: 'E',
        180: 'S',
        270: 'W'}

if __name__ == '__main__':
    with open('day12.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

        x, y = 0, 0
        dir = 90
        start_time = time.time()

        #nice_print(rows)
        for line in lines:
            command = line[0]
            value = int(line[1:])
            if command in ['N', 'E', 'S', 'W']:
                x, y = execute_command(command, value, x, y)
            elif command == 'R':
                print(f'R {value}')
                dir = (dir + value) % 360
            elif command == 'L':
                print(f'L {value}')
                dir = (dir - value) % 360
            elif command == 'F':
                print(dir)
                print(dir_to_cmd[dir])
                x, y = execute_command(dir_to_cmd[dir], value, x, y)

        manhattan_distance = abs(x) + abs(y)
        print(f'Final solution = {manhattan_distance}')
        print(f'Total time = {time.time() - start_time}')

