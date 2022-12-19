#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import re
import sys

def maxGeodesOpened(blueprint, time):
	_, oreRobotOreCost, clayRobotOreCost, obsidianRobotOreCost, obsidianRobotClayCost, geodeRobotOreCost, geodeRobotObsidianCost = blueprint
	maxOreCost = max(oreRobotOreCost, clayRobotOreCost, obsidianRobotOreCost, geodeRobotOreCost)
	q, bestResult = [(time, (1, 0, 0), (0, 0, 0, 0))], 0

	while q:
		remainingTime, (oreRobots, clayRobots, obsidianRobots), (ore, clay, obsidian, geodes) = q.pop()
		maxPotentialGeodesOpened = geodes + remainingTime * (remainingTime - 1) // 2

		if maxPotentialGeodesOpened < bestResult:
			continue

		if geodes > bestResult:
			bestResult = geodes

		if oreRobots < maxOreCost:
			skipTime = 1 + math.ceil(max(oreRobotOreCost - ore, 0) / oreRobots)

			if (newRemainingTime := remainingTime - skipTime) > 0:
				q.append((
					newRemainingTime,
					(oreRobots + 1, clayRobots, obsidianRobots),
					(
						ore + oreRobots * skipTime - oreRobotOreCost,
						clay + clayRobots * skipTime,
						obsidian + obsidianRobots * skipTime,
						geodes
					)
				))

		if clayRobots < obsidianRobotClayCost:
			skipTime = 1 + math.ceil(max(clayRobotOreCost - ore, 0) / oreRobots)

			if (newRemainingTime := remainingTime - skipTime) > 0:
				q.append((
					newRemainingTime,
					(oreRobots, clayRobots + 1, obsidianRobots),
					(
						ore + oreRobots * skipTime - clayRobotOreCost,
						clay + clayRobots * skipTime,
						obsidian + obsidianRobots * skipTime,
						geodes
					)
				))

		if clayRobots and obsidianRobots < geodeRobotObsidianCost:
			skipTime = 1 + max(
				math.ceil(max(obsidianRobotOreCost - ore, 0) / oreRobots),
				math.ceil(max(obsidianRobotClayCost - clay, 0) / clayRobots)
			)

			if (newRemainingTime := remainingTime - skipTime) > 0:
				q.append((
					newRemainingTime,
					(oreRobots, clayRobots, obsidianRobots + 1),
					(
						ore + oreRobots * skipTime - obsidianRobotOreCost,
						clay + clayRobots * skipTime - obsidianRobotClayCost,
						obsidian + obsidianRobots * skipTime,
						geodes
					)
				))

		if obsidianRobots:
			skipTime = 1 + max(
				math.ceil(max(geodeRobotOreCost - ore, 0) / oreRobots),
				math.ceil(max(geodeRobotObsidianCost - obsidian, 0) / obsidianRobots)
			)

			if (newRemainingTime := remainingTime - skipTime) > 0:
				q.append((
					newRemainingTime,
					(oreRobots, clayRobots, obsidianRobots),
					(
						ore + oreRobots * skipTime - geodeRobotOreCost,
						clay + clayRobots * skipTime,
						obsidian + obsidianRobots * skipTime - geodeRobotObsidianCost,
						geodes + newRemainingTime
					)
				))

	return bestResult

def solve(blueprints):
	return math.prod(maxGeodesOpened(blueprint, 32) for blueprint in blueprints)


if __name__ == '__main__':
	blueprints = [list(map(int, re.findall(r'\d+', line))) for line in sys.stdin.readlines()]

	print(solve(blueprints[:3]))
