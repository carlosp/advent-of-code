#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def isSafe(report: list[int]) -> bool:
	adjacentDiffRange = range(1, 4) if report[1] > report[0] else range(-3, 0)

	return all(
		report[idx] - report[idx - 1] in adjacentDiffRange
		for idx in range(1, len(report))
	)

def countSafeReports(reports: list[list[int]]) -> int:
	return sum(
		any(isSafe(report[:i] + report[i + 1:]) for i in range(len(report)))
		for report in reports
	)


if __name__ == '__main__':
	reports = [list(map(int, line.split())) for line in sys.stdin.readlines()]

	print(countSafeReports(reports))
