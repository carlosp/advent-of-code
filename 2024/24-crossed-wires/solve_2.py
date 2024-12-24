#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from dataclasses import dataclass
from enum import StrEnum
from typing import Self

class GateType(StrEnum):
	AND = 'AND'
	XOR = 'XOR'
	OR = 'OR'

@dataclass(frozen=True)
class Gate:
	input1: str
	input2: str
	type: GateType
	output: str

	@staticmethod
	def parse(s: str) -> Self:
		input1, type, input2, output = s.replace('->', '').split()
		return Gate(input1=input1, input2=input2, type=type, output=output)

	def getOtherInput(self, input: str) -> str:
		return self.input1 if input == self.input2 else self.input2

	def hasInput(self, input: str) -> bool:
		return input == self.input1 or input == self.input2


def solve(gates: list[Gate]) -> int:
	def findGate(type: GateType, input: str) -> Gate | None:
		return next((gate for gate in gates if gate.type == type and gate.hasInput(input)), None)

	swappedWires, bit, lastCarry = [], 0, findGate(GateType.AND, 'x00').output

	while len(swappedWires) != 8:
		'''
			Each bit is produced by a full adder (except the first, which is a half adder) implemented by
			the following gates, so we just need to find the wires not matching this implementation:

			x{bit} XOR y{bit} -> t1
			carry{bit - 1} XOR t1 -> z{bit}
			carry{bit - 1} AND t1 -> t2
			x{bit} AND y{bit} -> t3
			t2 OR t3 -> carry{bit}
		'''
		bit += 1
		xWire, zWire = 'x{:02}'.format(bit), 'z{:02}'.format(bit)
		t1 = findGate(GateType.XOR, xWire).output
		t2 = findGate(GateType.AND, lastCarry).output
		t3 = findGate(GateType.AND, xWire).output
		outputGate = findGate(GateType.XOR, lastCarry)
		orGate = findGate(GateType.OR, t2) or findGate(GateType.OR, t3)
		expectedT1 = outputGate.getOtherInput(lastCarry)
		lastCarry = orGate.output

		if t1 != expectedT1:
			swappedWires.append(t1)
		if outputGate.output != zWire:
			swappedWires.append(outputGate.output)
		if not orGate.hasInput(t2):
			swappedWires.append(t2)
		if not orGate.hasInput(t3):
			swappedWires.append(t3)
		if lastCarry == expectedT1 or lastCarry == zWire:
			swappedWires.append(lastCarry)
			lastCarry = swappedWires[-2]

	return ','.join(sorted(swappedWires))


if __name__ == '__main__':
	_, gatesDefinitions = sys.stdin.read().split('\n\n')
	gates = list(map(Gate.parse, gatesDefinitions.splitlines()))

	print(solve(gates))
