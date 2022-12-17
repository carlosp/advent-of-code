#!/usr/bin/env python3
# -*- coding: utf-8 -*-

CHAMBER_WIDTH = 7
NUM_ROCK_TYPES = 5

def getNextRock(rockNumber, y):
	match rockNumber % NUM_ROCK_TYPES:
		case 0: return [(2, y + 4), (3, y + 4), (4, y + 4), (5, y + 4)]
		case 1: return [(3, y + 4), (2, y + 5), (3, y + 5), (4, y + 5), (3, y + 6)]
		case 2: return [(2, y + 4), (3, y + 4), (4, y + 4), (4, y + 5), (4, y + 6)]
		case 3: return [(2, y + 4), (2, y + 5), (2, y + 6), (2, y + 7)]
		case 4: return [(2, y + 4), (3, y + 4), (2, y + 5), (3, y + 5)]

def getTowerHeight(jetPattern, numRocks):
	pushIdx, pushes = 0, list(map({ '<': -1, '>': 1 }.get, jetPattern))
	maxHeightsAtCol, maxHeight = [0] * CHAMBER_WIDTH, 0
	stateHistory, maxHeightHistory = {}, []
	filledTiles = set()

	for rockNumber in range(numRocks):
		maxHeightHistory += [maxHeight]
		stateKey = (rockNumber % NUM_ROCK_TYPES, pushIdx, tuple(maxHeight - y for y in maxHeightsAtCol))

		if stateKey in stateHistory:
			prevRockIdx = stateHistory[stateKey]
			prevMaxHeight = maxHeightHistory[prevRockIdx]
			cycleLength = rockNumber - prevRockIdx
			skipCycles = (numRocks - rockNumber) // cycleLength
			reminderCycles = (numRocks - rockNumber) % cycleLength

			return (maxHeight + skipCycles * (maxHeight - prevMaxHeight) +
					maxHeightHistory[prevRockIdx + reminderCycles] - prevMaxHeight)

		stateHistory[stateKey] = rockNumber
		rock, isRockMoving = getNextRock(rockNumber, maxHeight), True

		while isRockMoving:
			dx = pushes[pushIdx]
			pushIdx = (pushIdx + 1) % len(pushes)

			if all(0 <= x + dx < CHAMBER_WIDTH and (x + dx, y) not in filledTiles for x, y in rock):
				rock = [(x + dx, y) for x, y in rock]

			if all(y > 1 and (x, y - 1) not in filledTiles for x, y in rock):
				rock = [(x, y - 1) for x, y in rock]
			else:
				isRockMoving = False
				filledTiles.update(rock)

				for x, y in rock:
					maxHeightsAtCol[x] = max(y, maxHeightsAtCol[x])
					maxHeight = max(y, maxHeight)

	return maxHeight


if __name__ == '__main__':
	jetPattern = input().strip()

	print(getTowerHeight(jetPattern, 2022))
