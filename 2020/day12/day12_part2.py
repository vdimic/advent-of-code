#!/usr/bin/env python3
import time


def execute_command(cmd, val, x, y, wpx, wpy):
    print(f'{cmd} {val}')
    if cmd == 'N':
        return x, y, wpx, wpy + value
    elif cmd == 'E':
        return x, y, wpx + value, wpy
    elif cmd == 'S':
        return x, y, wpx, wpy - value
    elif cmd == 'W':
        return x, y, wpx - value, wpy
    else:
        print("FAIL")
        exit()

def execute_rotation(cmd, val, x, y, wpx, wpy):
    print(f'{cmd} {val}')
    if cmd == 'L':
        val = 360 - val
    if val == 90:
        return x, y, wpy, -wpx
    elif val == 180:
        return x, y, -wpx, -wpy
    elif val == 270:
        return x, y, -wpy, wpx
    else:
        print('FAIL')
        exit()

if __name__ == '__main__':
    with open('day12.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

        x, y = 0, 0
        wpx, wpy = 10, 1
        start_time = time.time()

        #nice_print(rows)
        for line in lines:
            command = line[0]
            value = int(line[1:])
            if command in ['N', 'E', 'S', 'W']:
                x, y, wpx, wpy = execute_command(command, value, x, y, wpx, wpy)
            elif command in ['R', 'L']:
                x, y, wpx, wpy = execute_rotation(command, value, x, y, wpx, wpy)
            elif command == 'F':
                x += wpx * value
                y += wpy * value
            #print(f'{x} {y}')

        manhattan_distance = abs(x) + abs(y)
        print(f'Final solution = {manhattan_distance}')
        print(f'Total time = {time.time() - start_time}')

