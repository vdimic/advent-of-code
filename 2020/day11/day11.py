#!/usr/bin/env python3
import copy
import itertools
import time

# Part 1
#SEAT_LIMIT = 4
# Part 2
SEAT_LIMIT = 5

def occupied_nearby_seats(rows, row, col):
    offsets_r = [0]
    if row > 0:
        offsets_r.append(-1)
    if row < len(rows) - 1:
        offsets_r.append(1)
    offsets_c = [0]
    if col > 0:
        offsets_c.append(-1)
    if col < len(rows[0]) - 1:
        offsets_c.append(1)
    sum = 0
    for dr, dc in itertools.product(offsets_r, offsets_c):
        if dr != 0 or dc != 0:
            sum += 1 if rows[row+dr][col+dc] == '#' else 0
    #print(f'{row} {col} {sum}')
    return sum

def occupied_visible_seats(rows, row, col):
    offsets = [-1, 0, 1]
    sum = 0
    for dr, dc in itertools.product(offsets, offsets):
        if dr == 0 and dc == 0:
            continue
        rr = row + dr
        cc = col + dc
        while rr >= 0 and rr < len(rows) and cc >= 0 and cc < len(rows[0]):
            if rows[rr][cc] == '.':
                rr += dr
                cc += dc
            elif rows[rr][cc] == 'L':
                break
            elif rows[rr][cc] == '#':
                sum += 1
                break
    return sum



def iterate(rows):
    changed = False
    rows_copy = copy.deepcopy(rows)
    for r, c in itertools.product(range(len(rows)), range(len(rows[0]))):
        if rows[r][c] == '.':
            continue
        # Part 1
        #occupied_seats = occupied_nearby_seats(rows, r, c)
        # Part 2
        occupied_seats = occupied_visible_seats(rows, r, c)
        if occupied_seats == 0:
            rows_copy[r][c] = '#'
            if rows[r][c] == 'L':
                changed = True
        elif occupied_seats >= SEAT_LIMIT:
            rows_copy[r][c] = 'L'
            if rows[r][c] == '#':
                changed = True
    return changed, copy.deepcopy(rows_copy)

def sum(rows):
    sum = 0
    for row in rows:
        for c in row:
            sum += 1 if c == '#' else 0
    return sum


def nice_print(rows):
    for row in rows:
        print(''.join(row))
    print('--------------')


if __name__ == '__main__':
    with open('day11.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        rows = [[ch for ch in line] for line in lines]
        start_time = time.time()

        #nice_print(rows)
        changed = False
        iter = 0
        while True:
            iter += 1
            print(iter)
            changed, rows = iterate(rows)
            #nice_print(rows)
            if not changed:
                break

        print(f'Final solution = {sum(rows)}')
        print(f'Total time = {time.time() - start_time}')

        start_time = time.time()
        print(f'Total time = {time.time() - start_time}')
