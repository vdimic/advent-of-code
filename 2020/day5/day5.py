#!/usr/bin/env python3


if __name__ == '__main__':
    with open('day5.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]

        #represent boarding pass number as binary number
        # F -> 0, B -> 1
        # R -> 1, L -> 0
        boarding_passes = [l.replace('F', '0').replace('B', '1').replace('R', '1').replace('L', '0') for l in lines]
        seat_ids = [int(bp, 2) for bp in boarding_passes]
        # Part 1
        print(max(seat_ids))
        
        # Part 2
        max_id = max(seat_ids)
        min_id = min(seat_ids)

        i = min_id
        while i <= max_id:
            if not i in seat_ids:
                print(i)
                break
            i += 1

