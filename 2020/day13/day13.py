#!/usr/bin/env python3
import functools
import time

def int_or_none(n):
    if n == 'x':
        return None
    else:
        return int(n)


if __name__ == '__main__':
    with open('day13.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        earliest_time = int(lines[0])
        bus_intervals = lines[1].split(',')
        buses = {id:int_or_none(interval) for id, interval in enumerate(bus_intervals) if int_or_none(interval)}
        print(buses)

        #Part 1
        start_time = time.time()
        from_arrival_to_departure = {id:(earliest_time % buses[id]) for id in buses if buses[id]}
        for k in from_arrival_to_departure:
            from_arrival_to_departure[k] = buses[k] - from_arrival_to_departure[k]
        print(f'from_arrival_to_departure {from_arrival_to_departure}')
        from_arrival_to_departure = dict(sorted(from_arrival_to_departure.items(), key=lambda x: x[1]))
        print(f'sorted from_arrival_to_departure {from_arrival_to_departure}')
        print(from_arrival_to_departure)


        print(f'Final solution = ')
        print(f'Total time = {time.time() - start_time}')

