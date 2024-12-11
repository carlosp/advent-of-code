#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import cache

def countStonesAfterBlinks(stones: list[int], blinks: int) -> int:
	@cache
	def count(stone: int, blinks: int) -> int:
		if blinks == 0:
			return 1
		elif stone == 0:
			return count(1, blinks - 1)
		elif (numDigits := len(str(stone))) % 2 == 0:
			return (
				count(stone // (10 ** (numDigits // 2)), blinks - 1) +
				count(stone % (10 ** (numDigits // 2)), blinks - 1)
			)
		else:
			return count(stone * 2024, blinks - 1)


	return sum(count(stone, blinks) for stone in stones)

if __name__ == '__main__':
	stones = list(map(int, input().split()))

	print(countStonesAfterBlinks(stones, 75))
