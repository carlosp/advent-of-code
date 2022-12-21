#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import operator
import sys

ROOT = 'root'
HUMAN = 'humn'

class Monkey(object):
	def __init__(self, name):
		self.name = name

class NumberYellingMonkey(Monkey):
	def __init__(self, name, value):
		super().__init__(name)
		self.value = value

	def dependsOnHuman(self):
		return self.name == HUMAN

	def ground(self, expectedYell):
		return expectedYell

	def yell(self):
		return self.value

class MathOperationMonkey(Monkey):
	def __init__(self, name, operation, leftMonkey, rightMonkey):
		super().__init__(name)
		self.operation = operation
		self.leftMonkey = leftMonkey
		self.rightMonkey = rightMonkey

	def dependsOnHuman(self):
		return self.leftMonkey.dependsOnHuman() or self.rightMonkey.dependsOnHuman()

	def ground(self, expectedYell):
		leftMonkeyDependsOnHuman = self.leftMonkey.dependsOnHuman()
		monkeyDependingOnHuman, otherMonkey = (
			(self.leftMonkey, self.rightMonkey) if leftMonkeyDependsOnHuman
			else (self.rightMonkey, self.leftMonkey))

		match self.operation, leftMonkeyDependsOnHuman:
			case '+', _:      newExpectedYell = expectedYell - otherMonkey.yell()
			case '-', True:   newExpectedYell = expectedYell + otherMonkey.yell()
			case '-', False:  newExpectedYell = otherMonkey.yell() - expectedYell
			case '*', _:      newExpectedYell = expectedYell // otherMonkey.yell()
			case '/', True:   newExpectedYell = expectedYell * otherMonkey.yell()
			case '/', False:  newExpectedYell = otherMonkey.yell() // expectedYell

		return monkeyDependingOnHuman.ground(newExpectedYell)

	def yell(self):
		return {
			'+': operator.add,
			'-': operator.sub,
			'*': operator.mul,
			'/': operator.floordiv
		}[self.operation](self.leftMonkey.yell(), self.rightMonkey.yell())


def solveRiddle(monkeyJobs):
	def createMonkey(name):
		match monkeyJobs[name]:
			case [number]:            return NumberYellingMonkey(name, int(number))
			case [name1, op, name2]:  return MathOperationMonkey(name, op, createMonkey(name1), createMonkey(name2))


	return createMonkey(ROOT).ground(0)


if __name__ == '__main__':
	monkeyJobs = {
		parts[0][:-1] : parts[1:]
		for parts in map(str.split, sys.stdin.readlines())
	}

	monkeyJobs[ROOT][1] = '-'
	print(solveRiddle(monkeyJobs))
