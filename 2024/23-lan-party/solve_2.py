#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import sys

def getMaximumClique(graph: dict[str, set[str]]) -> set[str]:
	def bronKerbosch(current: set[str], potential: set[str], excluded: set[str], maximumClique: set[str]) -> set[str]:
		if not potential and not excluded:
			if len(current) > len(maximumClique):
				return current
		else:
			pivot = (potential | excluded).pop()

			for vertex in potential - graph[pivot]:
				maximumClique = bronKerbosch(current | set([vertex]), potential & graph[vertex], excluded & graph[vertex], maximumClique)
				potential.remove(vertex)
				excluded.add(vertex)

		return maximumClique

	return bronKerbosch(set(), set(graph.keys()), set(), set())

def getLANPartyPassword(connections: list[tuple[str, str]]) -> str:
	graph = collections.defaultdict(set)

	for computer1, computer2 in connections:
		graph[computer1].add(computer2)
		graph[computer2].add(computer1)

	return ','.join(sorted(getMaximumClique(graph)))


if __name__ == '__main__':
	connections = list(tuple(line.strip().split('-')) for line in sys.stdin.readlines())

	print(getLANPartyPassword(connections))
