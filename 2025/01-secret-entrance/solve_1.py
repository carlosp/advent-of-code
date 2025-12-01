#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

DIAL_START = 50
DIAL_NUMBERS = 100

def getPassword(rotations: list[tuple[bool, int]]) -> int:
	dial, password = DIAL_START, 0

	for isClockwise, distance in rotations:
		if isClockwise:
			dial = (dial + distance) % DIAL_NUMBERS
		else:
			dial = (dial - distance) % DIAL_NUMBERS

		password += dial == 0

	return password


if __name__ == '__main__':
	rotations = [(line[0] == 'R', int(line[1:])) for line in sys.stdin.readlines()]

	print(getPassword(rotations))
