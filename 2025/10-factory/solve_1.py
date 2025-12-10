#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import sys
from functools import reduce
from operator import xor

def calculateFewestPressesToConfigureLights(lightDiagram: str, buttonSchematics: list[tuple[int, ...]]) -> int:
	target = sum(1 << len(lightDiagram) - idx - 1 for idx, state in enumerate(lightDiagram) if state == '#')
	buttons = [sum(1 << len(lightDiagram) - n - 1 for n in buttons) for buttons in buttonSchematics]

	for numClicks in range(1, len(buttons)):
		for buttonsPressed in itertools.combinations(buttons, numClicks):
			if reduce(xor, buttonsPressed) == target:
				return numClicks

	return len(buttons)

def calculateFewestPressesToConfigureMachines(machines: list[tuple[str, list[tuple[int, ...]]]]) -> int:
	return sum(
		calculateFewestPressesToConfigureLights(lightDiagram, buttonSchematics)
		for lightDiagram, buttonSchematics in machines
	)


if __name__ == '__main__':
	machines = [
		(
			lightDiagram[1:-1],
			[tuple(map(int, s[1:-1].split(','))) for s in buttonSchematics]
		)
		for lightDiagram, *buttonSchematics, _ in [line.strip().split() for line in sys.stdin.readlines()]
	]

	print(calculateFewestPressesToConfigureMachines(machines))
