#!/usr/bin/env python3

if __name__ == '__main__':
    with open('day3.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        print(lines)
        trees = 0
        # Part 1
        for row in range(len(lines)):
            col = (row * 3) % len(lines[row])
            if lines[row][col] == '#':
                trees += 1
        print(trees)

        # Part 2
        xy_offsets = [(1,1), (3,1), (5,1), (7,1), (1,2)]
        prod = 1
        for xy_offset in xy_offsets:
            x_offset = xy_offset[0]
            y_offset = xy_offset[1]
            x_pos = 0
            y_pos = 0
            trees = 0
            while y_pos < len(lines):
                if lines[y_pos][x_pos] == '#':
                    trees += 1
                x_pos = (x_pos + x_offset) % len(lines[0])
                y_pos += y_offset
            prod *= trees

        print(prod)
