#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def countScratchcards(scratchcards):
	copies = [1] * len(scratchcards)

	for idx, scratchcard in enumerate(scratchcards):
		winningNumbers, myNumbers = map(set, map(str.split, scratchcard.split(':')[1].split('|')))
		myWinningNumbers = winningNumbers & myNumbers

		for delta in range(len(myWinningNumbers)):
			copies[idx + delta + 1] += copies[idx]

	return sum(copies)


if __name__ == '__main__':
	print(countScratchcards(sys.stdin.readlines()))
