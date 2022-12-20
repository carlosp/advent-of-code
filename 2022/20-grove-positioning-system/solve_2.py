#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

MIX_ROUNDS = 10
DECRYPTION_KEY = 811589153

def decrypt(encryptedFile):
	numbers = [number * DECRYPTION_KEY for number in encryptedFile]
	indices = list(range(len(numbers)))

	for _ in range(MIX_ROUNDS):
		for idx, number in enumerate(numbers):
			currentPosition = indices.index(idx)
			newPosition = (currentPosition + number) % (len(numbers) - 1)
			indices.pop(currentPosition)
			indices.insert(newPosition, idx)

	return [numbers[idx] for idx in indices]

def getGroveCoordinates(encryptedFile):
	decryptedFile = decrypt(encryptedFile)
	zeroIndex = decryptedFile.index(0)

	return sum(decryptedFile[(zeroIndex + delta) % len(encryptedFile)] for delta in [1000, 2000, 3000])


if __name__ == '__main__':
	encryptedFile = list(map(int, sys.stdin.readlines()))

	print(getGroveCoordinates(encryptedFile))
