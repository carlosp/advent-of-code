#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def parseLiteralPacket(binData, idx, _):
	data = ''
	while True:
		data += binData[idx + 1:idx + 5]
		idx += 5

		if binData[idx - 5] == '0':
			break

	return idx, 0

def parseOperatorPacket(binData, idx, _):
	lengthType = binData[idx]
	idx += 1
	result = 0

	if lengthType == '0':
		lengthInBits = int(binData[idx:idx + 15], 2)
		idx += 15
		end = idx + lengthInBits

		while idx < end:
			idx, subresult = parsePacket(binData, idx)
			result += subresult
	else:
		numSubpackages = int(binData[idx: idx + 11], 2)
		idx += 11

		for _ in range(numSubpackages):
			idx, subresult = parsePacket(binData, idx)
			result += subresult

	return idx, result

def parsePacket(binData, idx):
	version = int(binData[idx:idx + 3], 2)
	type = int(binData[idx + 3:idx + 6], 2)
	idx, subresult = [parseOperatorPacket, parseLiteralPacket][type == 4](binData, idx + 6, type)

	return idx, version + subresult

def solve(hexData):
	binData = bin(int(hexData, 16))[2:].zfill(4 * len(hexData))

	return parsePacket(binData, 0)[1]


if __name__ == '__main__':
	hexData = input()

	print(solve(hexData))
