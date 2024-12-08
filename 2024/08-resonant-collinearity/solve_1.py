#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import itertools
import sys

def countLocationsWithAntinodes(map: list[str]) -> int:
	height, width = len(map), len(map[0])
	antennasByFrequency = collections.defaultdict(list)
	antinodes = set()

	for row in range(height):
		for col in range(width):
			if (frequency := map[row][col]) != '.':
				antennasByFrequency[frequency].append(complex(row, col))

	for antennasWithSameFrequency in antennasByFrequency.values():
		for antenna1, antenna2 in itertools.permutations(antennasWithSameFrequency, r=2):
			if (direction := antenna2 - antenna1):
				antenna2 += direction

				if 0 <= antenna2.real < height and 0 <= antenna2.imag < width:
					antinodes.add(antenna2)

	return len(antinodes)


if __name__ == '__main__':
	map = list(map(str.strip, sys.stdin.readlines()))

	print(countLocationsWithAntinodes(map))
