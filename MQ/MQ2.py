#include "MQ2.h"
# Ported from https://github.com/amperka/TroykaMQ
# Author: Alexey Tveritinov [kartun@yandex.ru]
from BaseMQ import BaseMQ 
from micropython import const

""" Clean air coefficient """
MQ2_RO_BASE = float(9.83)

class MQ2(BaseMQ):
	def __init__(self, pinData, pinHeater=-1, boardResistance = 10, baseVoltage = 5.0):
		# Call superclass to fill attributes
		super().__init__(pinData, pinHeater, boardResistance, baseVoltage)
		pass

	def readLPG(self):
		return self.readScaled(-0.45, 2.95)
		
	def readMethane(self):
		return self.readScaled(-0.38, 3.21)

	def readSmoke(self):
		return self.readScaled(-0.42, 3.54)

	def readHydrogen(self):
		return self.readScaled(-0.48, 3.32)

	def getRoInCleanAir(self):
		return MQ2_RO_BASE