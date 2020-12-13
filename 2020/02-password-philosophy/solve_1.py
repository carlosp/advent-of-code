#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

Policy = collections.namedtuple('Policy', 'minTimes maxTimes letter')

def parseLine(line):
	rawPolicy, password = map(str.strip, line.split(':'))
	times, letter = rawPolicy.split(' ')
	minTimes, maxTimes = map(int, times.split('-'))

	return Policy(minTimes, maxTimes, letter), password

def isValid(policy, password):
	return policy.minTimes <= password.count(policy.letter) <= policy.maxTimes


if __name__ == '__main__':
	validPasswords = 0

	for policy, password in map(parseLine, sys.stdin.readlines()):
		if isValid(policy, password):
			validPasswords += 1

	print(validPasswords)
