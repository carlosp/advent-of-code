#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys

REQUIRED_FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

def isValid(passportData):
	fields = set(map(lambda x: x.split(':')[0], passportData.replace('\n', ' ').split(' ')))

	return REQUIRED_FIELDS <= fields

if __name__ == '__main__':
	passportsData = sys.stdin.read().split('\n\n')
	print(len([passportData for passportData in passportsData if isValid(passportData)]))
