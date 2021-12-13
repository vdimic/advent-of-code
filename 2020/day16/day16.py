#!/usr/bin/env python3
import time

class Rule:
    def __init__(self, line):
        tokens = line.split(':')
        self.name = tokens[0]
        tokens = tokens[1].strip().split(' ')
        self.intervals = []
        for token in tokens:
            if token != 'or':
                start, end = token.split('-')
                self.intervals.append((int(start), int(end)))
        print(self.intervals)

    def contains(self, num):
        for start, end in self.intervals:
            if num >= start and num <= end:
                return True
        return False

class Ticket:
    def __init__(self, line):
        self.fields = [int(n) for n in line.split(',')]

    def scan_error_rate(self, rules):
        # return None if none of the fields is invalid, otherwise return scan error rate
        scan_error = None
        for field in self.fields:
            found_ok_rule = False
            for rule in rules:
                if rule.contains(field):
                    found_ok_rule = True
                    break
            if not found_ok_rule:
                if not scan_error:
                    scan_error = field
                else:
                    scan_error += field
        return scan_error

def narrow_down(field_possibilities):
    while True:
        # find fields with only one possibility
        definite_fields = [i for i, fp in enumerate(field_possibilities) if len(fp) == 1]
        print(f'definite fields {definite_fields}')
        # Remove that possibility from all other fields
        changed = False
        for definite_field in definite_fields:
            rule_to_remove = field_possibilities[definite_field][0]
            print(f'rule to remove {rule_to_remove}')
            for i, fp in enumerate(field_possibilities):
                if definite_field != i:
                    if rule_to_remove in fp:
                        changed = True
                        print('removing')
                        print(fp)
                        fp.remove(rule_to_remove)
                        print(fp)
        # Repeat until all fields have exactly one possibility
        # In other words, until none of the possibilities are removed
        if not changed:
            break



if __name__ == '__main__':
    with open('day16.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        state = 'rules' # 'my ticket' 'other tickets'
        rules = []
        tickets = []
        for line in lines:
            if line == '':
                continue
            if state == 'rules':
                if line == 'your ticket:':
                    state = 'my ticket'
                    continue
                rules.append(Rule(line))
            elif state == 'my ticket':
                #Parse my ticket
                if line == 'nearby tickets:':
                    state = 'other tickets'
                    continue
                my_ticket = Ticket(line)
            elif state == 'other tickets':
                tickets.append(Ticket(line))

        # Part 1
        start_time = time.time()
        total_scan_error_rate = 0
        valid_tickets = []
        for ticket in tickets:
            scan_error = ticket.scan_error_rate(rules)
            if not scan_error is None:
                total_scan_error_rate += scan_error
            else:
                valid_tickets.append(ticket)
        print(f'Final solution part 1 = {total_scan_error_rate}')
        print(f'Total time = {time.time() - start_time}')

        # Part 2
        start_time = time.time()
        field_possibilities = [[] for _ in range(len(valid_tickets[0].fields))]
        for fi in range(len(field_possibilities)):
            for rule in rules:
                all_fields_match_rule = True
                for ticket in valid_tickets:
                    if not rule.contains(ticket.fields[fi]):
                        all_fields_match_rule = False
                if all_fields_match_rule:
                    field_possibilities[fi].append(rule.name)
        print(field_possibilities)
        narrow_down(field_possibilities)
        print(field_possibilities)

        for i, fp in enumerate(field_possibilities):
            #if any(['departure' in r for r in fp]):
            print(f'{i} {fp}')

        departure_fields = [i for i, f in enumerate(field_possibilities) if 'departure' in f[0]]
        print(departure_fields)
        product = 1
        for f in departure_fields:
            product *= my_ticket.fields[f]
        print(f'Final solution part 2 = {product}')
        print(f'Total time = {time.time() - start_time}')
