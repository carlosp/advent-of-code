#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

HEIGHT, WIDTH = 103, 101
SECONDS = 100

def calculateSafetyFactor(robots: list[tuple[int, int, int, int]]) -> int:
	for _ in range(SECONDS):
		for idx, (x, y, dx, dy) in enumerate(robots):
			nextX, nextY = (x + dx) % WIDTH, (y + dy) % HEIGHT
			robots[idx] = (nextX, nextY, dx, dy)

	return (
		sum(x < WIDTH // 2 and y < HEIGHT // 2 for x, y, *_ in robots) *
		sum(x > WIDTH // 2 and y < HEIGHT // 2 for x, y, *_ in robots) *
		sum(x < WIDTH // 2 and y > HEIGHT // 2 for x, y, *_ in robots) *
		sum(x > WIDTH // 2 and y > HEIGHT // 2 for x, y, *_ in robots)
	)


if __name__ == '__main__':
	robots = [tuple(map(int, re.compile(r'-?\d+').findall(line))) for line in sys.stdin.readlines()]

	print(calculateSafetyFactor(robots))
