#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import scipy
import sys

def calculateFewestPressesToConfigureMachines(machines: list[tuple[tuple[int, ...], list[tuple[int, ...]]]]) -> int:
	numClicks = 0

	for joltageRequirements, buttonSchematics in machines:
		coefficients = [1] * len(buttonSchematics)
		constraints = [
			[counter in button for button in buttonSchematics]
			for counter in range(len(joltageRequirements))
		]
		lowerBounds = upperBounds = joltageRequirements
		numClicks += scipy.optimize.milp(
			c=coefficients,
			integrality=coefficients,
			constraints=[constraints, lowerBounds, upperBounds]
		).fun

	return int(numClicks)


if __name__ == '__main__':
	machines = [
		(
			tuple(map(int, joltageRequirements[1:-1].split(','))),
			[tuple(map(int, s[1:-1].split(','))) for s in buttonSchematics]
		)
		for _, *buttonSchematics, joltageRequirements in [line.strip().split() for line in sys.stdin.readlines()]
	]

	print(calculateFewestPressesToConfigureMachines(machines))
