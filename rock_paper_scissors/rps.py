#!/usr/bin/python

import sys
import math


def rock_paper_scissors(n):

    def rec_rps(n_current, n_total, cur_perm=None):
        rps0 = [["rock"],["paper"],["scissors"]]
        next_perm = []
        if n_total == 0:
            return [[]]
        elif n_total == 1:
            return rps0
        else:
            if (n_current <= 0) & (n_total != 0):
                return rec_rps(n_current + 1, n_total, next_perm)
            elif n_current == 1:
                return rec_rps(n_current + 1, n_total, rps0)
            elif n_current > 1:
                for i in range(3 ** (n_current-1)):
                    to_app = (cur_perm[i] if len(cur_perm) > 0 else [""])
                    next_perm.append(to_app + rps0[0])
                    next_perm.append(to_app + rps0[1])
                    next_perm.append(to_app + rps0[2])
            if n_current == n_total:
                return next_perm
            else:
                return rec_rps(n_current + 1, n_total, next_perm)

    return rec_rps(0, n)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')