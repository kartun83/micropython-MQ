#include "MQ2.h"
# Ported from https://github.com/amperka/TroykaMQ
# Author: Alexey Tveritinov [kartun@yandex.ru]
from BaseMQ import BaseMQ 
from micropython import const

class MQ2(BaseMQ):
	## Clean air coefficient
	MQ2_RO_BASE = float(9.83)

	def __init__(self, pinData, pinHeater=-1, boardResistance = 10, baseVoltage = 5.0, measuringStrategy = BaseMQ.STRATEGY_ACCURATE):
		# Call superclass to fill attributes
		super().__init__(pinData, pinHeater, boardResistance, baseVoltage, measuringStrategy)
		pass

	## Measure liquefied hydrocarbon gas, LPG
	def readLPG(self):
		return self.readScaled(-0.45, 2.95)
		
	## Measure methane	
	def readMethane(self):
		return self.readScaled(-0.38, 3.21)

	## Measure smoke
	def readSmoke(self):
		return self.readScaled(-0.42, 3.54)

	## Measure hydrogen
	def readHydrogen(self):
		return self.readScaled(-0.48, 3.32)

    ##  Base RO differs for every sensor family
	def getRoInCleanAir(self):
		return self.MQ2_RO_BASE