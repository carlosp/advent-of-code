#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io

class BinaryStringIO(io.StringIO):
	def read(_, *args):
		return int(super().read(*args), 2)

def parseLiteralPacket(binStream):
	lastPrefix = 1

	while lastPrefix:
		lastPrefix = binStream.read(1)
		binStream.read(4)

	return 0

def parseOperatorPacket(binStream):
	lengthType = binStream.read(1)
	result = 0

	if lengthType == 0:
		lengthInBits = binStream.read(15)
		end = binStream.tell() + lengthInBits

		while binStream.tell() < end:
			result += parsePacket(binStream)
	else:
		numSubpackages = binStream.read(11)

		for _ in range(numSubpackages):
			result += parsePacket(binStream)

	return result

def parsePacket(binStream):
	version = binStream.read(3)
	type = binStream.read(3)

	return version + [parseOperatorPacket, parseLiteralPacket][type == 4](binStream)

def solve(hexData):
	binData = bin(int(hexData, 16))[2:].zfill(4 * len(hexData))

	return parsePacket(BinaryStringIO(binData))


if __name__ == '__main__':
	hexData = input()

	print(solve(hexData))
