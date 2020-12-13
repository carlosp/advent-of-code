#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

Policy = collections.namedtuple('Policy', 'pos1 pos2 letter')

def parseLine(line):
	rawPolicy, password = map(str.strip, line.split(':'))
	positions, letter = rawPolicy.split(' ')
	pos1, pos2 = map(int, positions.split('-'))

	return Policy(pos1, pos2, letter), password

def isValid(policy, password):
	return (password[policy.pos1 - 1] == policy.letter) ^ (password[policy.pos2 - 1] == policy.letter)


if __name__ == '__main__':
	validPasswords = 0

	for policy, password in map(parseLine, sys.stdin.readlines()):
		if isValid(policy, password):
			validPasswords += 1

	print(validPasswords)
