#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import networkx as nx
import re
import sys

BAG_TYPE_RE = re.compile(r' ?(?:\d+ )?([a-z ]+) bags?')

def parseRule(rule):
	rawBagTypes = re.split('contain|,', rule)

	return list(map(lambda x: BAG_TYPE_RE.search(x).group(1), rawBagTypes))

def buildGraph(rules):
	graph = nx.DiGraph()

	for container, *containees in map(parseRule, rules):
		for containee in containees:
			graph.add_edge(containee, container)

	return graph

def solve(rules):
	graph = buildGraph(rules)

	return len(nx.algorithms.dag.descendants(graph, 'shiny gold'))


if __name__ == '__main__':
	print(solve(sys.stdin.readlines()))
