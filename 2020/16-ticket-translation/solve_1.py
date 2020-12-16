#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def parseRange(range):
	return tuple(map(int, range.split('-')))

def parseRules(rules):
	parsedRules = []

	for rule in rules:
		field, ranges = rule.split(':')
		range1, range2 = map(parseRange, ranges.split('or'))
		parsedRules += [(field, range1, range2)]

	return parsedRules

def parseTickets(tickets):
	parsedTickets = []

	for ticket in tickets[1:]:
		parsedTickets += [list(map(int, ticket.split(',')))]

	return parsedTickets

def sumOfInvalidFields(rules, tickets):
	sum = 0

	for ticket in tickets:
		for value in ticket:
			isValid = False

			for _, range1, range2 in rules:
				if range1[0] <= value <= range1[1] or range2[0] <= value <= range2[1]:
					isValid = True
					break

			if not isValid:
				sum += value

	return sum

def solve(rules, myTicket, otherTickets):
	rules = parseRules(rules)
	tickets = parseTickets(myTicket) + parseTickets(otherTickets)

	return sumOfInvalidFields(rules, tickets)


if __name__ == '__main__':
	rules, myTicket, otherTickets = map(lambda x: x.strip().split('\n'), sys.stdin.read().split('\n\n'))
	print(solve(rules, myTicket, otherTickets))
