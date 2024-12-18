#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import bisect
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

def findFirstBytePositionBlockingPath(incomingBytesPositions: list[tuple[int, int]]) -> tuple[int, int]:
	idx = bisect.bisect(range(len(incomingBytesPositions)), False,
						key=lambda idx: countMinStepsToExit(incomingBytesPositions[:idx + 1]) is None)

	return incomingBytesPositions[idx]


if __name__ == '__main__':
	incomingBytesPositions = [tuple(map(int, line.split(','))) for line in sys.stdin.readlines()]

	print(*findFirstBytePositionBlockingPath(incomingBytesPositions), sep=',')
