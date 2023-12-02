#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

MAX_CUBES = {
	'red'	: 12,
	'green'	: 13,
	'blue'	: 14
}

def checkGameFeasibility(gameInfo):
	gameIdInfo, subsetsOfCubesList = gameInfo.split(':')
	gameId = int(gameIdInfo.split(' ')[1])

	for subsetsOfCubes in subsetsOfCubesList.split(';'):
		for subsetOfCubes in subsetsOfCubes.split(','):
			numCubes, color = subsetOfCubes.strip().split(' ')

			if int(numCubes) > MAX_CUBES[color]:
				return gameId, False

	return gameId, True


if __name__ == '__main__':
	print(sum(
		gameId
		for gameId, isGamePossible in map(checkGameFeasibility, sys.stdin.readlines())
		if isGamePossible
	))
