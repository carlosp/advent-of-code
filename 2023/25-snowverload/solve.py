#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
import networkx as nx
import sys

def solve(graph):
	minCut = nx.minimum_edge_cut(graph)

	graph.remove_edges_from(minCut)

	return math.prod(map(len, nx.connected_components(graph)))


if __name__ == '__main__':
	graph = nx.parse_adjlist([line.strip().replace(':', '') for line in sys.stdin.readlines()])

	print(solve(graph))
