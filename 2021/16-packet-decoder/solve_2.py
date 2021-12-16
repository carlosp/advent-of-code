#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import operator

def parseLiteralPacket(binData, idx, _):
	data = ''
	while True:
		data += binData[idx + 1:idx + 5]
		idx += 5

		if binData[idx - 5] == '0':
			break

	return idx, int(data, 2)

def parseOperatorPacket(binData, idx, packageType):
	lengthType = binData[idx]
	idx += 1
	subresults = []

	if lengthType == '0':
		lengthInBits = int(binData[idx:idx + 15], 2)
		idx += 15
		end = idx + lengthInBits

		while idx < end:
			idx, subresult = parsePacket(binData, idx)
			subresults += [subresult]
	else:
		numSubpackages = int(binData[idx: idx + 11], 2)
		idx += 11

		for _ in range(numSubpackages):
			idx, subresult = parsePacket(binData, idx)
			subresults += [subresult]

	match packageType:
		case 0: result = sum(subresults)
		case 1: result = math.prod(subresults)
		case 2: result = min(subresults)
		case 3: result = max(subresults)
		case 5: result = operator.gt(*subresults)
		case 6: result = operator.lt(*subresults)
		case 7: result = operator.eq(*subresults)

	return idx, result

def parsePacket(binData, idx):
	_ = int(binData[idx:idx + 3], 2)
	type = int(binData[idx + 3:idx + 6], 2)

	return [parseOperatorPacket, parseLiteralPacket][type == 4](binData, idx + 6, type)

def solve(hexData):
	binData = bin(int(hexData, 16))[2:].zfill(4 * len(hexData))

	return parsePacket(binData, 0)[1]


if __name__ == '__main__':
	hexData = input()

	print(solve(hexData))
