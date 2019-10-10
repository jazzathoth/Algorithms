#!/usr/bin/python

import argparse


def find_max_profit(prices):
    best = prices[1] - prices[0]
    for i1 in range(len(prices)):
        start = i1
        end = len(prices)
        for i2 in range(start + 1, end):
            current = prices[i2] - prices[start]
            if current > best:
                best = current
    return best


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))