#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import heapq
from dataclasses import dataclass

@dataclass
class File:
	id: int
	position: int
	length: int

def calculateChecksum(files: list[File]) -> int:
	return sum(
		file.id * (2 * file.position + file.length - 1) * file.length // 2
		for file in files
	)

def compactFiles(files: list[File], freeSpacesByLength: list[list[int]]) -> None:
	for file in reversed(files):
		candidateFreeSpaces = [
			(freeSpacesByLength[length][0], length)
			for length in range(file.length, len(freeSpacesByLength))
			if freeSpacesByLength[length] and freeSpacesByLength[length][0] < file.position
		]

		if candidateFreeSpaces:
			freeSpacePosition, freeSpaceLength = min(candidateFreeSpaces)
			file.position = freeSpacePosition
			heapq.heappop(freeSpacesByLength[freeSpaceLength])

			if newLength := freeSpaceLength - file.length:
				heapq.heappush(freeSpacesByLength[newLength], freeSpacePosition + file.length)

def parseDiskMap(diskMap: str) -> tuple[list[File], list[list[int]]]:
	files, freeSpacesByLength = [], [[] for _ in range(10)]
	position = 0

	for idx, length in enumerate(map(int, diskMap)):
		if idx % 2 == 0:
			files.extend(File(id=idx // 2, position=position + i, length=1) for i in range(length))
		elif length:
			heapq.heappush(freeSpacesByLength[length], position)

		position += length

	return files, freeSpacesByLength


def solve(diskMap: str) -> int:
	files, freeSpacesByLength = parseDiskMap(diskMap)

	compactFiles(files, freeSpacesByLength)

	return calculateChecksum(files)


if __name__ == '__main__':
	diskMap = input()

	print(solve(diskMap))
