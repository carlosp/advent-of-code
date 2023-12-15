#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import functools

def hash(string):
	return functools.reduce(lambda x, y: (17 * (x + ord(y))) % 256, string, 0)


if __name__ == '__main__':
	print(sum(map(hash, input().split(','))))
