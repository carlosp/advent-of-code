#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

PRUNE_MOD = 16777216
SEQUENCE_BASE = 20
SEQUENCE_MOD = SEQUENCE_BASE ** 4

def solve(secrets: list[int]) -> int:
	bananasForSequence = collections.defaultdict(int)

	for secret in secrets:
		sequence, seenSequences = 0, set()

		for idx in range(2000):
			lastPrice = secret % 10
			secret = ((secret * 64) ^ secret) % PRUNE_MOD
			secret = ((secret // 32) ^ secret) % PRUNE_MOD
			secret = ((secret * 2048) ^ secret) % PRUNE_MOD
			currentPrice = secret % 10
			sequence = (SEQUENCE_BASE * sequence + 10 + currentPrice - lastPrice) % SEQUENCE_MOD

			if idx >= 3 and sequence not in seenSequences:
				seenSequences.add(sequence)
				bananasForSequence[sequence] += currentPrice

	return max(bananasForSequence.values())


if __name__ == '__main__':
	secrets = list(map(int, sys.stdin.readlines()))

	print(solve(secrets))
