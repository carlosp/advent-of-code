#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
import sys
from functools import cache
from scipy.signal import convolve2d

def enhanceImage(algorithm, image, enhanceSteps):
	kernel = np.array([1 << idx for idx in range(9)]).reshape(3, 3)
	imageFromAlgorithmIndices = np.vectorize(cache(lambda idx: algorithm[idx]))

	fillValue = 0
	for _ in range(enhanceSteps):
		algorithmIndices = convolve2d(image, kernel, fillvalue=fillValue)
		image = imageFromAlgorithmIndices(algorithmIndices)
		fillValue = algorithm[(0, -1)[fillValue]]

	return image

def countLitPixelsAfterEnhancingImage(algorithm, image, enhanceSteps):
	parsePixel = lambda pixel: int(pixel == '#')
	image = np.array([list(map(parsePixel, row)) for row in image])
	algorithm = list(map(parsePixel, algorithm))

	return np.sum(enhanceImage(algorithm, image, enhanceSteps))


if __name__ == '__main__':
	algorithm, _ = input(), input()
	image = [line.strip() for line in sys.stdin.readlines()]

	print(countLitPixelsAfterEnhancingImage(algorithm, image, 2))
