#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

CARD_STRENGTH_ORDER = 'AKQT98765432J'
HAND_STRENGTH_BY_TWO_MOST_COMMON_CARD_COUNTS = {
	(5, 0): 1,
	(4, 1): 2,
	(3, 2): 3,
	(3, 1): 4,
	(2, 2): 5,
	(2, 1): 6,
	(1, 1): 7
}

def handSortKey(hand):
	cardsInHand = collections.Counter(hand)

	if jokerCount := cardsInHand['J']:
		jokerReplacement = next((card for card, _ in cardsInHand.most_common() if card != 'J'), 'A')
		cardsInHand[jokerReplacement] += jokerCount
		del cardsInHand['J']

	mostCommonCards = cardsInHand.most_common()
	twoMostCommonCardCounts = mostCommonCards[0][1], 0 if len(mostCommonCards) == 1 else mostCommonCards[1][1]

	return HAND_STRENGTH_BY_TWO_MOST_COMMON_CARD_COUNTS[twoMostCommonCardCounts], *map(CARD_STRENGTH_ORDER.index, hand)

def calculateTotalWinnings(bidsByHand):
	rankedHands = sorted(bidsByHand.keys(), key=handSortKey, reverse=True)

	return sum(rank * int(bidsByHand[hand]) for rank, hand in enumerate(rankedHands, 1))

if __name__ == '__main__':
	bidsByHand = dict(map(str.split, sys.stdin.readlines()))

	print(calculateTotalWinnings(bidsByHand))
