#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def solve(earliestDepart, buses):
	buses = set(map(int, set(buses) - set(['x'])))
	bus, waitTime = min([(bus - earliestDepart % bus, bus) for bus in buses])

	return bus * waitTime


if __name__ == '__main__':
	earliestDepart = int(input())
	buses = input().split(',')
	print(solve(earliestDepart, buses))
