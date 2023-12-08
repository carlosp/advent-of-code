#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import math
import re
import sys

NODE_NAME_RE = re.compile(r'\w{3}')

def countStepsToReachEndNode(instructions, network, node):
	for step, direction in enumerate(itertools.cycle(instructions)):
		if node.endswith('Z'):
			return step

		node = network[node][direction == 'R']

def countStepsToBeOnlyOnEndNodes(instructions, network):
	# Not a general solution: it assumes the number of steps from a given start node to its first encountered end node
	# is the same as from each end node in its path to the next one.
	return math.lcm(*(
		countStepsToReachEndNode(instructions, network, startNode)
		for startNode in network
		if startNode.endswith('A')
	))


if __name__ == '__main__':
	instructions, _ = input(), input()
	network = {
		node: (left, right)
		for node, left, right in map(NODE_NAME_RE.findall, sys.stdin.readlines())
	}

	print(countStepsToBeOnlyOnEndNodes(instructions, network))
