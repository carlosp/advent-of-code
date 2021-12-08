#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

ALL_SEGMENTS = 'abcdefg'
NUMBER_WITH_SEGMENTS = {
	'abcefg'	: '0',
	'cf'		: '1',
	'acdeg'		: '2',
	'acdfg'		: '3',
	'bcdf'		: '4',
	'abdfg'		: '5',
	'abdefg'	: '6',
	'acf'		: '7',
	'abcdefg'	: '8',
	'abcdfg'	: '9'
}

def filterByLength(length, patterns):
	return next(pattern for pattern in patterns if len(pattern) == length)

def filterByLengthAndSomeSegmentExcluded(length, segmentsToExcludeSome, patterns):
	return next(pattern for pattern in patterns
		if len(pattern) == length and any(segment not in pattern for segment in segmentsToExcludeSome))

def extractSegments(lengthForCandidates, segmentsToExclude, patterns):
	maybeX, maybeY = set(filterByLength(lengthForCandidates, patterns)) - set(segmentsToExclude)
	patternWithXAndNotY = filterByLengthAndSomeSegmentExcluded(6, [maybeX, maybeY], patterns)
	return (maybeX, maybeY) if maybeX in patternWithXAndNotY else (maybeY, maybeX)

def solve(entries):
	def processEntry(entry):
		signalPatterns, outputValue = map(str.split, entry.split('|'))

		f, c = extractSegments(2, [], signalPatterns)
		a, = set(filterByLength(3, signalPatterns)) - set([c, f])
		b, d = extractSegments(4, [c, f], signalPatterns)
		g, e = extractSegments(7, [a, b, c, d, f], signalPatterns)
		translation = str.maketrans(a + b + c + d + e + f + g, ALL_SEGMENTS)

		return int(''.join(
			NUMBER_WITH_SEGMENTS[''.join(sorted(segments.translate(translation)))]
			for segments in outputValue
		))

	return sum(map(processEntry, entries))


if __name__ == '__main__':
	entries = sys.stdin.readlines()
	print(solve(entries))
