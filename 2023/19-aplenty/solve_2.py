#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import sys

CATEGORIES = 'xmas'

def parseWorkflow(workflowDefinition):
	name, ruleDefinitions = workflowDefinition[:-1].split('{')
	rules = []

	for ruleDefinition in ruleDefinitions.split(','):
		if ':' in ruleDefinition:
			value, nextWorkflowName = ruleDefinition[2:].split(':')
			rules += [(ruleDefinition[0], ruleDefinition[1], int(value), nextWorkflowName)]
		else:
			rules += [ruleDefinition]

	return name, rules

def getAcceptedRatings(workflows, workflowName, candidateRatings):
	if workflowName == 'A':
		return [candidateRatings]

	if workflowName == 'R':
		return []

	acceptedRatings = []

	for rule in workflows[workflowName]:
		match rule:
			case category, op, value, nextWorkflowName:
				rangeStart, rangeEnd = candidateRatings[category]

				if op == '<':
					matchedStart, matchedEnd = min(rangeStart, value), min(rangeEnd, value)
					unmatchedStart, unmatchedEnd = max(rangeStart, value), max(rangeEnd, value)
				else:
					matchedStart, matchedEnd = max(rangeStart, value + 1), max(rangeEnd, value + 1)
					unmatchedStart, unmatchedEnd = min(rangeStart, value + 1), min(rangeEnd, value + 1)

				acceptedRatings += getAcceptedRatings(workflows, nextWorkflowName, {
					**candidateRatings,
					category: (matchedStart, matchedEnd)
				})
				candidateRatings[category] = (unmatchedStart, unmatchedEnd)
			case _:
				acceptedRatings += getAcceptedRatings(workflows, rule, candidateRatings)

	return acceptedRatings

def solve(workflows):
	candidateRatings = { category: (1, 4001) for category in CATEGORIES }
	acceptedRatings = getAcceptedRatings(workflows, 'in', candidateRatings)

	return sum(
		math.prod((rangeEnd - rangeStart) for rangeStart, rangeEnd in acceptedRating.values())
		for acceptedRating in acceptedRatings
	)


if __name__ == '__main__':
	workflowDefinitions, partRatingsDefinitions = sys.stdin.read().split('\n\n')
	workflows = dict(map(parseWorkflow, workflowDefinitions.splitlines()))

	print(solve(workflows))
