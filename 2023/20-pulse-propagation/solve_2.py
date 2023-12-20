#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import collections
import math
import sys

LOW_PULSE = False
HIGH_PULSE = True

Pulse = collections.namedtuple('Pulse', 'type source destination')

class Module(object):
	@staticmethod
	def parse(moduleDefinition):
		name, destinations = moduleDefinition.strip().split(' -> ')
		destinations = destinations.split(', ')

		match name:
			case 'broadcaster':           return BroadcastModule(name, destinations)
			case name if name[0] == '%':  return FlipFlopModule(name[1:], destinations)
			case name if name[0] == '&':  return ConjuntionModule(name[1:], destinations)

	def __init__(self, name, destinations):
		self.name = name
		self.destinations = destinations

	def emitPulse(self, pulseType):
		return [Pulse(pulseType, self.name, destination) for destination in self.destinations]

	def processPulse(self, _):
		raise NotImplementedError

class BroadcastModule(Module):
	def processPulse(self, pulse):
		return self.emitPulse(pulse.type)

class FlipFlopModule(Module):
	def __init__(self, name, destinations):
		super().__init__(name, destinations)

		self.on = False

	def processPulse(self, pulse):
		if pulse.type == LOW_PULSE:
			self.on = not self.on
			return self.emitPulse(self.on)

		return []

class ConjuntionModule(Module):
	def __init__(self, name, destinations):
		super().__init__(name, destinations)

		self.lastPulsesBySource = {}

	def addInput(self, moduleName):
		self.lastPulsesBySource[moduleName] = LOW_PULSE

	def processPulse(self, pulse):
		self.lastPulsesBySource[pulse.source] = pulse.type
		newPulseType = any(pulseType == LOW_PULSE for pulseType in self.lastPulsesBySource.values())

		return self.emitPulse(newPulseType)


def parseModules(moduleDefinitions):
	modules = { module.name: module for module in map(Module.parse, moduleDefinitions) }

	for module in modules.values():
		for destination in module.destinations:
			if (destinationModule := modules.get(destination, None)) and type(destinationModule) == ConjuntionModule:
				destinationModule.addInput(module.name)

	return modules

def pushButton(modules, iteration, modulesToWatchForHighPulse):
	pendingPulses = collections.deque([Pulse(LOW_PULSE, 'button', 'broadcaster')])

	while pendingPulses:
		pulse = pendingPulses.popleft()

		if pulse.type == HIGH_PULSE and modulesToWatchForHighPulse.get(pulse.source, 0) is None:
			modulesToWatchForHighPulse[pulse.source] = iteration

		if pulse.destination in modules:
			pendingPulses.extend(modules[pulse.destination].processPulse(pulse))

def solve(modules):
	# Not a general solution: it assumes there is a single conjunction module before rx,
	# which has only other conjuntion modules as sources.

	lastModuleBeforeRx = next(module for module in modules.values() if 'rx' in module.destinations)
	firstIterationWithHighPulseBySource = { source: None for source in lastModuleBeforeRx.lastPulsesBySource.keys() }
	iteration = 0

	while any(iteration is None for iteration in firstIterationWithHighPulseBySource.values()):
		pushButton(modules, iteration := iteration + 1, firstIterationWithHighPulseBySource)

	return math.lcm(*firstIterationWithHighPulseBySource.values())


if __name__ == '__main__':
	modules = parseModules(sys.stdin.readlines())

	print(solve(modules))
