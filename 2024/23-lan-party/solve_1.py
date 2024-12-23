#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

def countValidTriangles(graph: dict[str, set[str]]) -> int:
	return len(set(
		computers
		for computer1 in graph
		for computer2 in graph[computer1]
		for computer3 in graph[computer1] & graph[computer2]
		if (computers := frozenset((computer1, computer2, computer3))) and any(computer.startswith('t') for computer in computers)
	))

def solve(connections: list[tuple[str, str]]) -> int:
	graph = collections.defaultdict(set)

	for computer1, computer2 in connections:
		graph[computer1].add(computer2)
		graph[computer2].add(computer1)

	return countValidTriangles(graph)


if __name__ == '__main__':
	connections = list(tuple(line.strip().split('-')) for line in sys.stdin.readlines())

	print(solve(connections))
