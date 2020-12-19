#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from lark import Lark
import sys

def buildParser(rules):
	grammar = ''

	for rule in rules:
		ruleId, ruleDescription = rule.split(':')
		ruleConditions = []

		for subcondition in map(str.strip, ruleDescription.split('|')):
			if subcondition[0] != '"':
				subcondition = ' '.join(map(lambda x: 'rule' + x, subcondition.split(' ')))

			ruleConditions += [subcondition]

		grammar += 'rule{} : {}\n'.format(ruleId, ' | '.join(ruleConditions))

	return Lark(grammar, start='rule0')

def isValid(parser, message):
	try:
		parser.parse(message)
		return True
	except:
		return False

def solve(rules, messages):
	parser = buildParser(rules)
	return sum(1 for message in messages if isValid(parser, message))


if __name__ == '__main__':
	rules, messages = map(lambda x: x.strip().split('\n'), sys.stdin.read().split('\n\n'))
	print(solve(rules, messages))
