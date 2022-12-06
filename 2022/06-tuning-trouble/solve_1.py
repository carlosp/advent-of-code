#!/usr/bin/env python3
# -*- coding: utf-8 -*-

WINDOW_SIZE = 4

def getPositionOfFirstStartOfPacketMarker(signal):
	for idx in range(len(signal)):
		if idx >= WINDOW_SIZE - 1 and len(set(signal[idx - WINDOW_SIZE + 1:idx + 1])) == WINDOW_SIZE:
			return idx + 1


if __name__ == '__main__':
	signal = input()

	print(getPositionOfFirstStartOfPacketMarker(signal))
