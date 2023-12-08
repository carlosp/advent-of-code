#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import itertools
import re
import sys

NODE_NAME_RE = re.compile(r'\w{3}')

def countStepsToReachEndNode(instructions, network):
	node = 'AAA'

	for step, direction in enumerate(itertools.cycle(instructions)):
		if node == 'ZZZ':
			return step

		node = network[node][direction == 'R']


if __name__ == '__main__':
	instructions, _ = input(), input()
	network = {
		node: (left, right)
		for node, left, right in map(NODE_NAME_RE.findall, sys.stdin.readlines())
	}

	print(countStepsToReachEndNode(instructions, network))
