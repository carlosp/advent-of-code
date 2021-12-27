#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

BLOCK_SIZE = 18
CONSTANTS_INDICES = [4, 5, 15]

def extractConstants(monad):
	constants = (
		[int(monad[BLOCK_SIZE * blockIdx + instructionIdx][-1]) for instructionIdx in CONSTANTS_INDICES]
		for blockIdx in range(len(monad) // BLOCK_SIZE)
	)

	return zip(*constants)

def largestValidModelNumber(monad):
	zDivs, xAdds, yAdds = extractConstants(monad)
	inputs = [9] * len(zDivs)
	stack = []

	for idx in range(len(zDivs)):
		if zDivs[idx] == 1:
			stack.append(idx)
		else:
			lastIdx = stack.pop()
			delta = yAdds[lastIdx] + xAdds[idx]
			inputs[lastIdx] -= max(0, delta)
			inputs[idx] += min(0, delta)

	return ''.join(map(str, inputs))


if __name__ == '__main__':
	monad = [line.strip().split() for line in sys.stdin.readlines()]
	print(largestValidModelNumber(monad))
