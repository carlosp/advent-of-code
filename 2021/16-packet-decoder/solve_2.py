#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
import math
import operator

class BinaryStringIO(io.StringIO):
	def read(_, *args):
		return int(super().read(*args), 2)

def parseLiteralPacket(binStream, _):
	data, lastPrefix = 0, 1

	while lastPrefix:
		lastPrefix = binStream.read(1)
		data = 16 * data + binStream.read(4)

	return data

def parseOperatorPacket(binStream, packageType):
	lengthType = binStream.read(1)
	subresults = []

	if lengthType == 0:
		lengthInBits = binStream.read(15)
		end = binStream.tell() + lengthInBits

		while binStream.tell() < end:
			subresults += [parsePacket(binStream)]
	else:
		numSubpackages = binStream.read(11)

		for _ in range(numSubpackages):
			subresults += [parsePacket(binStream)]

	match packageType:
		case 0: result = sum(subresults)
		case 1: result = math.prod(subresults)
		case 2: result = min(subresults)
		case 3: result = max(subresults)
		case 5: result = operator.gt(*subresults)
		case 6: result = operator.lt(*subresults)
		case 7: result = operator.eq(*subresults)

	return int(result)

def parsePacket(binStream):
	_ = binStream.read(3)
	type = binStream.read(3)

	return [parseOperatorPacket, parseLiteralPacket][type == 4](binStream, type)

def solve(hexData):
	binData = bin(int(hexData, 16))[2:].zfill(4 * len(hexData))

	return parsePacket(BinaryStringIO(binData))


if __name__ == '__main__':
	hexData = input()

	print(solve(hexData))
