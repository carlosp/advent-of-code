#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

MAX_COORDINATE = 70

def countMinStepsToExit(incomingBytesPositions: list[tuple[int, int]]) -> int | None:
	pendingPositions = (
		{ complex(x, y) for x in range(MAX_COORDINATE + 1) for y in range(MAX_COORDINATE + 1) if x or y } -
		{ complex(x, y) for x, y in incomingBytesPositions }
	)
	queue = collections.deque([(0, complex(0, 0))])

	while queue:
		steps, position = queue.popleft()

		if position == complex(MAX_COORDINATE, MAX_COORDINATE):
			return steps

		for direction in [1, -1, 1j, -1j]:
			nextPosition = position + direction

			if nextPosition in pendingPositions:
				pendingPositions.remove(nextPosition)
				queue.append((steps + 1, nextPosition))


if __name__ == '__main__':
	incomingBytesPositions = [tuple(map(int, line.split(','))) for line in sys.stdin.readlines()]

	print(countMinStepsToExit(incomingBytesPositions[:1024]))
