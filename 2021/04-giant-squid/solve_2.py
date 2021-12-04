#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def getBoardScore(board, numbers):
	uncheckedCounts = [[len(board)] * 2 for _ in range(len(board))]
	uncheckedSum = 0
	numberPositions = {}

	for rowIdx, row in enumerate(board):
		for colIdx, number in enumerate(row):
			uncheckedSum += number
			numberPositions[number] = (rowIdx, colIdx)

	for idx, number in enumerate(number for number in numbers if number in numberPositions):
		row, col = numberPositions[number]
		uncheckedCounts[row][0] -= 1
		uncheckedCounts[col][1] -= 1
		uncheckedSum -= number

		if uncheckedCounts[row][0] == 0 or uncheckedCounts[col][1] == 0:
			return idx, uncheckedSum * number


if __name__ == '__main__':
	numbers = list(map(int, input().split(',')))
	rawBoards = sys.stdin.readlines()
	boards = [
		list(map(lambda x: list(map(int, x.strip().split())), rawBoards[i + 1:i + 6]))
		for i in range(0, len(rawBoards), 6)
	]
	print(max(map(lambda board: getBoardScore(board, numbers), boards))[1])
