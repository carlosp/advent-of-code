#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

PRUNE_MOD = 16777216

def solve(secrets: list[int]) -> int:
	result = 0

	for secret in secrets:
		for _ in range(2000):
			secret = ((secret * 64) ^ secret) % PRUNE_MOD
			secret = ((secret // 32) ^ secret) % PRUNE_MOD
			secret = ((secret * 2048) ^ secret) % PRUNE_MOD

		result += secret

	return result


if __name__ == '__main__':
	secrets = list(map(int, sys.stdin.readlines()))

	print(solve(secrets))
