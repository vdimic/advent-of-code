#!/usr/bin/env python3
import copy

class Instruction:
    def __init__(self, op, val):
        self.op = op
        self.val = int(val)

    def __str__(self):
        return f'{self.op} {self.val}'

def parse_code(lines):
    code = []
    for line in lines:
        op, val = line.split()
        code.append(Instruction(op, val))
    return code

def execute_instruction(ins, pc, acc):
    if ins.op == 'acc':
        return pc + 1, acc + ins.val
    elif ins.op == 'nop':
        return pc + 1, acc
    elif ins.op == 'jmp':
        return pc + ins.val, acc

if __name__ == '__main__':
    with open('day8.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        code = parse_code(lines)
        print(code)

        # Part 1
        pc = 0
        acc = 0
        executed = [False] * len(code)
        while pc < len(code):
            if executed[pc]:
                break
            else:
                executed[pc] = True
                pc, acc = execute_instruction(code[pc], pc, acc)

        print(f'Acc = {acc}')

        # Part 2
        for change_i in range(len(code)):
            changed_code = copy.deepcopy(code)
            if code[change_i].op == 'jmp':
                changed_code[change_i].op = 'nop'
            elif code[change_i].op == 'nop':
                changed_code[change_i].op = 'jmp'
            else:
                continue
            # Execute changed program
            pc = 0
            acc = 0
            executed = [False] * len(code)
            while pc < len(code):
                if executed[pc]:
                    break
                else:
                    executed[pc] = True
                    pc, acc = execute_instruction(changed_code[pc], pc, acc)
            if pc == len(code):
                print(f'acc = {acc}')
                exit()
