#!/usr/bin/env python3


if __name__ == '__main__':
    with open('day6.txt', 'r') as f:
        lines = [l.strip() for l in f.readlines()]
        # Part 1
        total_common_true_answers = 0
        group_answers = [False] * 26
        for line in lines:
            if line == '':
                common_true_answers = sum(group_answers)
                total_common_true_answers += common_true_answers
                group_answers = [False] * 26
            else:
                # decode one person's answers:
                answer = [False] * 26
                for c in line:
                    answer[ord(c) - ord('a')] = True
                group_answers = [g or a for g, a in zip(group_answers, answer)]
        print(total_common_true_answers)

        # Part 2
        total_common_true_answers = 0
        group_answers = [True] * 26
        for line in lines:
            if line == '':
                common_true_answers = sum(group_answers)
                total_common_true_answers += common_true_answers
                group_answers = [True] * 26
            else:
                # decode one person's answers:
                answer = [False] * 26
                for c in line:
                    answer[ord(c) - ord('a')] = True
                group_answers = [g and a for g, a in zip(group_answers, answer)]
        print(total_common_true_answers)
