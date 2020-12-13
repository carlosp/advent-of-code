#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys

BAG_TYPE_RE = re.compile(r' ?(\d+ )?([a-z ]+) bags?')

def parseRule(rule):
	rawBagTypes = re.split('contain|,', rule)
	parts = []

	for rawBagType in rawBagTypes:
		quantity, parsedBagType = BAG_TYPE_RE.search(rawBagType).groups()

		if parsedBagType != 'no other':
			parts += [(int(quantity or 0), parsedBagType)]

	return parts[0][1], *parts[1:]

def buildGraph(rules):
	graph = {}

	for container, *containees in map(parseRule, rules):
		for quantity, containee in containees:
			graph[container] = graph.get(container, []) + [(quantity, containee)]

	return graph

def countTotalBags(graph, container):
	total = 1

	for quantity, containee in graph.get(container, []):
		total += quantity * countTotalBags(graph, containee)

	return total

def solve(rules):
	graph = buildGraph(rules)

	return countTotalBags(graph, 'shiny gold') - 1


if __name__ == '__main__':
	print(solve(sys.stdin.readlines()))
