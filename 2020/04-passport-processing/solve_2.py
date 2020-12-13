#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string
import sys

DIGITS = '0123456789'
HEX = DIGITS + 'abcdef'

def isIntBetween(x, start, endInclusive):
	return x.isdigit() and start <= int(x) <= endInclusive

def isValidHeight(x):
	return x[-2:] == 'cm' and isIntBetween(x[:-2], 150, 193) or \
			x[-2:] == 'in' and isIntBetween(x[:-2], 59, 76)

def isValidHairColor(x):
	return len(x) == 7 and x[0] == '#' and all(c in HEX for c in x[1:])

def isValidEyeColor(x):
	return x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def isValidPassportId(x):
	return len(x) == 9 and all(c in DIGITS for c in x)


FIELD_VALIDATORS = {
	'byr': lambda x: isIntBetween(x, 1920, 2002),
	'iyr': lambda x: isIntBetween(x, 2010, 2020),
	'eyr': lambda x: isIntBetween(x, 2020, 2030),
	'hgt': isValidHeight,
	'hcl': isValidHairColor,
	'ecl': isValidEyeColor,
	'pid': isValidPassportId
}


def isValid(passportData):
	fieldsData = list(map(lambda x: x.split(':'), passportData.replace('\n', ' ').strip().split(' ')))
	fieldsDataMap = {data[0]: data[1] for data in fieldsData}

	for fieldName, fieldValidator in FIELD_VALIDATORS.items():
		if fieldName not in fieldsDataMap or not fieldValidator(fieldsDataMap[fieldName]):
			return False

	return True


if __name__ == '__main__':
	passportsData = sys.stdin.read().split('\n\n')
	print(len([passportData for passportData in passportsData if isValid(passportData)]))
