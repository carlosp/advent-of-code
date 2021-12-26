#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from functools import cache
from heapq import heappop, heappush

ENERGY_PER_MOVE = [0, 1, 10, 100, 1000]
HALLWAY_ROOM_POSITIONS = [0, 2, 4, 6, 8]
VALID_HALLWAY_STOPS = [0, 1, 3, 5, 7, 9, 10]
ROOM_SIZE = 2

class Hallway(int):
	def getAmphipod(self, position):
		return (self >> (3 * position)) & 7

	def setAmphipod(self, position, amphipod):
		mask = ~(7 << (3 * position))
		return Hallway((self & mask) | (amphipod << (3 * position)))

	def isClear(self, fromPosition, toPosition):
		return not (self >> (3 * fromPosition)) & ((1 << (3 * (toPosition - fromPosition + 1))) - 1)

class Room(int):
	def __new__(cls, type, value):
		self = int.__new__(cls, value)
		self.type = type
		self.isOrganized = value == 11 * type
		self.freeSize = ROOM_SIZE if value == 0 else ROOM_SIZE - len(str(value))
		self.containsIncorrectAmphipod = value and any(int(x) != type for x in str(value))
		self.lastAmphipod = value % 10
		return self

	def addAmphipod(self, amphipod):
		return Room(self.type, 10 * self + amphipod)

	def removeLastAmphipod(self):
		return Room(self.type, self // 10)

class Burrow:
	def __init__(self, hallway, rooms):
		self.hallway = hallway
		self.rooms = rooms

	def isOrganized(self):
		return all(room.isOrganized for room in self.rooms)

	def canMoveFromHallwayToFinalRoom(self, fromHallwayPosition):
		if (amphipod := self.hallway.getAmphipod(fromHallwayPosition)) and not self.rooms[amphipod - 1].containsIncorrectAmphipod:
			toHallwayPosition = HALLWAY_ROOM_POSITIONS[amphipod]
			if fromHallwayPosition < toHallwayPosition:
				fromHallwayPosition, toHallwayPosition = fromHallwayPosition + 1, toHallwayPosition - 1
			else:
				fromHallwayPosition, toHallwayPosition = toHallwayPosition + 1, fromHallwayPosition - 1

			return self.hallway.isClear(fromHallwayPosition, toHallwayPosition)

	def moveFromHallwayToFinalRoom(self, fromHallwayPosition):
		amphipod = self.hallway.getAmphipod(fromHallwayPosition)
		room = self.rooms[amphipod - 1].addAmphipod(amphipod)
		return self._move(fromHallwayPosition, 0, room, amphipod)

	def canMoveFromRoomToHallway(self, room, toHallwayPosition):
		fromHallwayPosition = HALLWAY_ROOM_POSITIONS[room.type]
		if fromHallwayPosition < toHallwayPosition:
			fromHallwayPosition, toHallwayPosition = fromHallwayPosition + 1, toHallwayPosition
		else:
			fromHallwayPosition, toHallwayPosition = toHallwayPosition, fromHallwayPosition - 1

		return self.hallway.isClear(fromHallwayPosition, toHallwayPosition)

	def moveFromRoomToHallway(self, room, toHallwayPosition):
		amphipod = room.lastAmphipod
		return self._move(toHallwayPosition, amphipod, room.removeLastAmphipod(), amphipod)

	def _move(self, hallwayPosition, amphipodAtHallway, room, amphipodMoved):
		newHallway = self.hallway.setAmphipod(hallwayPosition, amphipodAtHallway)
		newRooms = self.rooms[:room.type - 1] + (room,) + self.rooms[room.type:]
		moves = abs(hallwayPosition - HALLWAY_ROOM_POSITIONS[room.type]) + room.freeSize + int(amphipodAtHallway == 0)
		return ENERGY_PER_MOVE[amphipodMoved] * moves, Burrow(newHallway, newRooms)

	def __eq__(self, other):
		return self.hallway == other.hallway and self.rooms == other.rooms

	def __hash__(self):
		return hash((self.hallway, self.rooms))


@cache
def minEnergyToOrganizeAmphipods(burrow):
	if burrow.isOrganized():
		return 0

	for hallwayPosition in VALID_HALLWAY_STOPS:
		if burrow.canMoveFromHallwayToFinalRoom(hallwayPosition):
			newCost, newBurrow = burrow.moveFromHallwayToFinalRoom(hallwayPosition)
			return newCost + minEnergyToOrganizeAmphipods(newBurrow)

	minCost = 2**64
	for room in burrow.rooms:
		if room.containsIncorrectAmphipod:
			for hallwayPosition in VALID_HALLWAY_STOPS:
				if burrow.canMoveFromRoomToHallway(room, hallwayPosition):
					newCost, newBurrow = burrow.moveFromRoomToHallway(room, hallwayPosition)
					minCost = min(minCost, newCost + minEnergyToOrganizeAmphipods(newBurrow))

	return minCost


if __name__ == '__main__':
	lines = sys.stdin.readlines()
	amphipodRows = [[line[idx] for idx in [3, 5, 7, 9]] for line in lines[2:-1]]
	amphipodCols = tuple(''.join(reversed(x)) for x in zip(*amphipodRows))
	amphipodToInt = str.maketrans('ABCD', '1234')
	rooms = tuple(
		Room(idx, int(amphipodStr.translate(amphipodToInt)))
		for idx, amphipodStr in enumerate(amphipodCols, 1)
	)
	burrow = Burrow(Hallway(), rooms)

	print(minEnergyToOrganizeAmphipods(burrow))
