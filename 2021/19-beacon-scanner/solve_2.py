#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

ORIENTATION_SIGNS = [
	(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1),
	(-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)
] * 3
ORIENTATION_AXES = [
	(0, 1, 2), (0, 2, 1), (0, 2, 1), (0, 1, 2),
	(0, 2, 1), (0, 1, 2), (0, 1, 2), (0, 2, 1),
	(1, 2, 0), (1, 0, 2), (1, 0, 2), (1, 2, 0),
	(1, 0, 2), (1, 2, 0), (1, 2, 0), (1, 0, 2),
	(2, 0, 1), (2, 1, 0), (2, 1, 0), (2, 0, 1),
	(2, 1, 0), (2, 0, 1), (2, 0, 1), (2, 1, 0)
]
ORIENTATIONS = list(zip(ORIENTATION_SIGNS, ORIENTATION_AXES))

class ScannerReport:
	def __init__(self, beacons):
		self.beaconsByOrientation = {}
		self.alignedBeacons = beacons
		self.alignedPosition = None

		for orientation in ORIENTATIONS:
			(signX, signY, signZ), (x, y, z) = orientation
			self.beaconsByOrientation[orientation] = [
				(signX * beacon[x], signY * beacon[y], signZ * beacon[z])
				for beacon in beacons
			]

	def alignIfPossible(self, other):
		for orientation in ORIENTATIONS:
			distances = {}
			for x1, y1, z1 in self.beaconsByOrientation[orientation]:
				for x2, y2, z2 in other.alignedBeacons:
					distance = (x2 - x1, y2 - y1, z2 - z1)
					distances[distance] = distances.get(distance, 0) + 1

					if distances[distance] == 12:
						self.alignedPosition = distance
						self.alignedBeacons = [
							(x + distance[0], y + distance[1], z + distance[2])
							for x, y, z in self.beaconsByOrientation[orientation]
						]

						return True


def solve(scannerReports):
	queue = [scannerReports[0]]
	scannerReports[0].position = (0, 0, 0)

	while queue:
		alignedReport = queue.pop()

		for otherReport in scannerReports:
			if not otherReport.alignedPosition and otherReport.alignIfPossible(alignedReport):
				queue.append(otherReport)

	return max(
		sum(abs(s1.alignedPosition[x] - s2.alignedPosition[x]) for x in [0, 1, 2])
		for s1 in scannerReports
		for s2 in scannerReports
	)


if __name__ == '__main__':
	reports = sys.stdin.read().split('\n\n')
	scannerReports = [
		ScannerReport([
			tuple(map(int, line.split(',')))
			for line in report.splitlines()[1:]
		])
		for report in reports
	]
	print(solve(scannerReports))
