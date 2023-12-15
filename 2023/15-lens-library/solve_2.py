#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import functools

def hash(string):
	return functools.reduce(lambda x, y: (17 * (x + ord(y))) % 256, string, 0)

def calculateFocusingPower(initSequence):
	boxes = collections.defaultdict(collections.OrderedDict)

	for step in initSequence:
		if step[-1] == '-':
			label = step[:-1]
			boxNumber = hash(label)
			boxes[boxNumber].pop(label, None)
		else:
			label, focalLength = step[:-2], int(step[-1])
			boxNumber = hash(label)
			boxes[boxNumber][label] = focalLength

	return sum(
		(boxNumber + 1) * lensSlot * focalLength
		for boxNumber, lensSlots in boxes.items()
		for lensSlot, (_, focalLength) in enumerate(lensSlots.items(), 1)
	)


if __name__ == '__main__':
	print(calculateFocusingPower(input().split(',')))
