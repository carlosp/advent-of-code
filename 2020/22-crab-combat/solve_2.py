#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def state(deck):
	return ','.join(map(str, deck))

def recursiveCombat(deck1, deck2, history1, history2):
	while deck1 and deck2:
		state1, state2 = state(deck1), state(deck2)

		if state1 in history1 and state2 in history2:
			return 1

		history1.add(state1)
		history2.add(state2)

		card1, card2 = deck1.pop(0), deck2.pop(0)
		if len(deck1) >= card1 and len(deck2) >= card2:
			winner = recursiveCombat(deck1[:card1], deck2[:card2], set(), set())
		else:
			winner = 1 if card1 > card2 else 2

		if winner == 1:
			deck1.append(card1)
			deck1.append(card2)
		else:
			deck2.append(card2)
			deck2.append(card1)

	return 1 if deck1 else 2

def score(deck):
	return sum(card * (idx + 1) for idx, card in enumerate(reversed(deck)))

def solve(decks):
	deck1 = list(map(int, decks[0].split('\n')[1:]))
	deck2 = list(map(int, decks[1].split('\n')[1:]))
	winner = recursiveCombat(deck1, deck2, set(), set())

	return score(deck1) if winner == 1 else score(deck2)


if __name__ == '__main__':
	print(solve(sys.stdin.read().strip().split('\n\n')))
