#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import operator
import sys
from collections import namedtuple

NUM_ROUNDS = 10000
Monkey = namedtuple('Monkey', ['id', 'items', 'operation', 'test', 'ifTrue', 'ifFalse'])

def parseOperation(operation):
	op1, op, op2 = operation.split('=')[1].strip().split()
	op = {
		'+': operator.add,
		'*': operator.mul
	}[op]

	if op1 == op2:
		return lambda item, *_: op(item, item)
	else:
		v = int(op1) if op2 == 'old' else int(op2)
		return lambda item, v=v: op(item, v)

def parseNotes(notes):
	monkeys = [None] * len(notes)

	for monkeyAttributes in notes:
		monkeyId = int(monkeyAttributes[0].split(':')[0].split()[1])
		items = list(map(int, monkeyAttributes[1].split(':')[1].split(',')))
		operation = parseOperation(monkeyAttributes[2])
		test = int(monkeyAttributes[3].split()[-1])
		ifTrue = int(monkeyAttributes[4].split()[-1])
		ifFalse = int(monkeyAttributes[5].split()[-1])

		monkeys[monkeyId] = Monkey(monkeyId, items, operation, test, ifTrue, ifFalse)

	return monkeys

def getLevelOfMonkeyBusiness(notes):
	monkeys = parseNotes(notes)
	inspections = [0] * len(monkeys)
	mod = math.prod(monkey.test for monkey in monkeys)

	for _ in range(NUM_ROUNDS):
		for monkey in monkeys:
			for item in monkey.items:
				item = monkey.operation(item) % mod
				nextMonkey = [monkey.ifFalse, monkey.ifTrue][item % monkey.test == 0]
				monkeys[nextMonkey].items.append(item)

			inspections[monkey.id] += len(monkey.items)
			monkey.items.clear()

	return math.prod(sorted(inspections)[-2:])


if __name__ == '__main__':
	notes = list(map(str.splitlines, sys.stdin.read().split('\n\n')))

	print(getLevelOfMonkeyBusiness(notes))
