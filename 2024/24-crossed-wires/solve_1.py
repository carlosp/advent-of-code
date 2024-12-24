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


def solve(wires: dict[str, bool], gates: list[Gate]) -> int:
	while gates:
		gate = gates.pop(0)

		if gate.input1 in wires and gate.input2 in wires:
			match gate.type:
				case GateType.AND: wires[gate.output] = wires[gate.input1] & wires[gate.input2]
				case GateType.XOR: wires[gate.output] = wires[gate.input1] ^ wires[gate.input2]
				case GateType.OR : wires[gate.output] = wires[gate.input1] | wires[gate.input2]
		else:
			gates.append(gate)

	outputWires = sorted(((wire, value) for wire, value in wires.items() if wire.startswith('z')), reverse=True)

	return int(''.join('01'[value] for _, value in outputWires), 2)


if __name__ == '__main__':
	wiresDefinitions, gatesDefinitions = sys.stdin.read().split('\n\n')
	wires = { wire[:-1]: value == '1' for wire, value in map(str.split, wiresDefinitions.splitlines()) }
	gates = list(map(Gate.parse, gatesDefinitions.splitlines()))

	print(solve(wires, gates))
