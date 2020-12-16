#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
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

def getValidTickets(rules, tickets):
	validTickets = []

	for ticket in tickets:
		validTicket = True

		for value in ticket:
			isValid = False

			for _, range1, range2 in rules:
				if range1[0] <= value <= range1[1] or range2[0] <= value <= range2[1]:
					isValid = True
					break

			if not isValid:
				validTicket = False
				break

		if validTicket:
			validTickets += [ticket]

	return validTickets

def getOrderedFields(rules, validTickets):
	orderedFields = [None] * len(rules)
	possibleFieldsForRules = [set(range(len(rules))) for _ in range(len(rules))]

	for ruleIdx, (_, range1, range2) in enumerate(rules):
		for ticket in validTickets:
			for fieldIdx, value in enumerate(ticket):
				if not (range1[0] <= value <= range1[1] or range2[0] <= value <= range2[1]):
					possibleFieldsForRules[ruleIdx].discard(fieldIdx)

	for _ in range(len(rules)):
		for ruleIdx, possibleFields in enumerate(possibleFieldsForRules):
			if len(possibleFields) == 1:
				fieldIdx = possibleFields.pop()
				orderedFields[fieldIdx] = rules[ruleIdx][0]
				break

		for possibleFields in possibleFieldsForRules:
			possibleFields.discard(fieldIdx)

	return orderedFields

def solve(rules, myTicket, otherTickets):
	rules = parseRules(rules)
	tickets = parseTickets(myTicket) + parseTickets(otherTickets)
	validTickets = getValidTickets(rules, tickets)
	orderedFields = getOrderedFields(rules, validTickets)

	return math.prod(value
		for fieldName, value in zip(orderedFields, tickets[0])
		if fieldName.startswith('departure'))


if __name__ == '__main__':
	rules, myTicket, otherTickets = map(lambda x: x.strip().split('\n'), sys.stdin.read().split('\n\n'))
	print(solve(rules, myTicket, otherTickets))
