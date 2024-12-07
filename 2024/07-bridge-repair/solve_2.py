#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

def isPossible(testValue: int, numbers: list[int]) -> bool:
	lastNumber = numbers.pop()
	strTestValue, strLastNumber = str(testValue), str(lastNumber)

	if len(numbers) == 0:
		return testValue == lastNumber

	return any([
		testValue >= lastNumber and isPossible(testValue - lastNumber, numbers.copy()),
		testValue % lastNumber == 0 and isPossible(testValue // lastNumber, numbers.copy()),
		strTestValue.endswith(strLastNumber) and isPossible(int('0' + strTestValue[:-len(strLastNumber)]), numbers.copy())
	])

def getCalibrationResult(equations: list[tuple[int, list[int]]]) -> int:
	return sum(testValue for testValue, numbers in equations if isPossible(testValue, numbers))

if __name__ == '__main__':
	equations = [
		(int(strTestValue[:-1]), list(map(int, strNumbers)))
		for strTestValue, *strNumbers in map(str.split, sys.stdin.readlines())
	]

	print(getCalibrationResult(equations))
