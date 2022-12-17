#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

class Cave(object):
	def __init__(self, report):
		self.numValves = len(report)
		self.flowRates = [None] * self.numValves
		self.graph = [None] * self.numValves
		self.valveNumbers = { valve: idx for idx, (valve, *_) in enumerate(report) }

		for valve, flowRate, adjacentValves in report:
			self.flowRates[self.valveNumbers[valve]] = flowRate
			self.graph[self.valveNumbers[valve]] = list(map(self.valveNumbers.get, adjacentValves))

		self.valvesWithFlow = [idx for idx in range(self.numValves) if self.flowRates[idx]]
		self._computeDistancesFloydWarshall()

	def getMaxPressureReleased(self, startingValve, maxTime):
		startingValveNumber = self.valveNumbers[startingValve]
		maxPressureReleasedByValvesOpen = self._getMaxPressureReleasedByOpenValves(startingValveNumber, maxTime, 0, 0, {})

		return max(
			pressureReleased1 + pressureReleased2
			for openValves1, pressureReleased1 in maxPressureReleasedByValvesOpen.items()
			for openValves2, pressureReleased2 in maxPressureReleasedByValvesOpen.items()
			if not openValves1 & openValves2
		)

	def _computeDistancesFloydWarshall(self):
		self.distances = [[self.numValves] * self.numValves for _ in range(self.numValves)]

		for valve, adjacentValves in enumerate(self.graph):
			self.distances[valve][valve] = 0

			for adjacentValve in adjacentValves:
				self.distances[valve][adjacentValve] = 1

		for k in range(self.numValves):
			for i in range(self.numValves):
				for j in range(self.numValves):
					if self.distances[i][j] > self.distances[i][k] + self.distances[k][j]:
						self.distances[i][j] = self.distances[i][k] + self.distances[k][j]

	def _getMaxPressureReleasedByOpenValves(self, currentValve, timeLeft, pressureReleased, openValves, results):
		results[openValves] = max(pressureReleased, results.get(openValves, 0))

		for valve in self.valvesWithFlow:
			if not openValves & (1 << valve):
				timeLeftAfterOpeningValve = timeLeft - self.distances[currentValve][valve] - 1

				if timeLeftAfterOpeningValve > 1:
					openValves = openValves | (1 << valve)
					results = self._getMaxPressureReleasedByOpenValves(valve, timeLeftAfterOpeningValve,
						pressureReleased + timeLeftAfterOpeningValve * self.flowRates[valve], openValves, results)
					openValves = openValves & ~(1 << valve)

		return results


if __name__ == '__main__':
	report = [
		(words[1], int(words[4][5:-1]), ''.join(words[9:]).split(','))
		for words in [line.strip().split(' ') for line in sys.stdin.readlines()]
	]

	print(Cave(report).getMaxPressureReleased('AA', 26))
