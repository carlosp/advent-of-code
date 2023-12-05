#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def applyMappings(seedRanges, maps):
	for map in maps:
		mappedRanges = []

		for mapStart, mapEnd, mapOffset in map:
			unmappedRanges = []

			for seedStart, seedEnd in seedRanges:
				if mapStart > seedEnd or mapEnd < seedStart:
					unmappedRanges += [(seedStart, seedEnd)]
				else:
					intersectionStart, intersectionEnd = max(seedStart, mapStart), min(seedEnd, mapEnd)

					mappedRanges += [(intersectionStart + mapOffset, intersectionEnd + mapOffset)]
					if seedStart < intersectionStart: unmappedRanges += [(seedStart, intersectionStart - 1)]
					if seedEnd > intersectionEnd: unmappedRanges += [(intersectionEnd + 1, seedEnd)]

			seedRanges = unmappedRanges

		seedRanges.extend(mappedRanges)

	return seedRanges

def parseMap(lines):
	return [
		(sourceRangeStart, sourceRangeStart + rangeLength - 1, destinationRangeStart - sourceRangeStart)
		for destinationRangeStart, sourceRangeStart, rangeLength in (map(int, line.split()) for line in lines.splitlines()[1:])
	]

def solve(almanac):
	seeds = map(int, almanac[0][7:].split(' '))
	maps = map(parseMap, almanac[1:])
	seedRanges = [(start, start) for start in seeds]

	return min(start for start, _ in applyMappings(seedRanges, maps))


if __name__ == '__main__':
	almanac = sys.stdin.read().split('\n\n')

	print(solve(almanac))
