#!/usr/bin/python

import sys


def rock_paper_scissors(n, acc=[[]]):
    if n == 0:
        return acc
    return rock_paper_scissors(n - 1, [[*i, j] for i in acc for j in ['rock', 'paper', 'scissors']])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
