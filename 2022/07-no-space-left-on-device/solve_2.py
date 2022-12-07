#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def parseTerminalOutput(terminalOutput):
	path = [{}]

	for line in terminalOutput:
		match line.split():
			case [_, 'cd', '/']:    del path[1:]
			case [_, 'cd', '..']:   path.pop()
			case [_, 'cd', dir]:    path += [path[-1].get(dir, {})]
			case ['$', 'ls']:       pass
			case ['dir', name]:     path[-1][name] = {}
			case [size, name]:      path[-1][name] = int(size)

	return path[0]

def computeDirectorySizes(root):
	result = []
	size = 0

	for item in root.values():
		if type(item) is dict:
			result += computeDirectorySizes(item)
			size += result[-1]
		else:
			size += item

	return result + [size]

def solve(terminalOutput):
	filesystemRoot = parseTerminalOutput(terminalOutput)
	directorySizes = computeDirectorySizes(filesystemRoot)

	return min(size for size in directorySizes if size >= directorySizes[-1] -  40000000)


if __name__ == '__main__':
	terminalOutput = sys.stdin.readlines()

	print(solve(terminalOutput))
