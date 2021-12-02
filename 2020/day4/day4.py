#!/usr/bin/env python3


class Passport:
    mandatory_fields = [
        'byr',
        'iyr',
        'eyr',
        'hgt',
        'hcl',
        'ecl',
        'pid',
        ]

    def __init__(self):
        self.byr = None #(Birth Year)
        self.iyr = None #(Issue Year)
        self.eyr = None #(Expiration Year)
        self.hgt = None #(Height)
        self.hcl = None #(Hair Color)
        self.ecl = None #(Eye Color)
        self.pid = None #(Passport ID)
        self.cid = None #(Country ID)

    def set_value(self, key, val):
        setattr(self, key, val)
        pass

    def valid(self):
        for mf in self.mandatory_fields:
            if getattr(self, mf) is None:
                return False
        return True

    def strictly_valid(self):
        if not self.valid():
            return False
        try:
            byr = int(self.byr)
            if byr < 1920 or byr > 2002:
                return False

            iyr = int(self.iyr)
            if iyr < 2010 or iyr > 2020:
                return False

            eyr = int(self.eyr)
            if eyr < 2020 or eyr > 2030:
                return False

            if not (self.hgt[-2:] == 'cm' and int(self.hgt[0:-2]) >= 150 and int(self.hgt[0:-2]) <= 193) and\
                not (self.hgt[-2:] == 'in' and int(self.hgt[0:-2]) >= 59 and int(self.hgt[0:-2]) <= 76):
                return False

            if not (self.hcl[0] == '#' and len(self.hcl[1:]) == 6 and int(self.hcl[1:], 16)):
                return False

            if not self.ecl in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False

            if not (len(self.pid) == 9 and int(self.pid)):
                return False
        except:
            return False

        return True

    def __str__(self):
        return ' '.join([f'{k}:{getattr(self, k)}' for k in self.mandatory_fields])

if __name__ == '__main__':
    with open('day4.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        p = Passport()
        valid_passports = 0
        strictly_valid_passports = 0
        for line in lines:
            if line == '':
                # Part 1
                print(f'{p}')
                if p.valid():
                    valid_passports += 1
                    print('t')
                # Part 2
                if p.strictly_valid():
                    strictly_valid_passports += 1
                    print('T')
                p = Passport()
            key_val_pairs = line.split()
            for key_val_pair in key_val_pairs:
                key, val = key_val_pair.split(':')
                p.set_value(key, val)
        print(valid_passports)
        print(strictly_valid_passports)
