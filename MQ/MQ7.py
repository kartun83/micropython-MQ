#include "MQ7.h"
# Ported from https://github.com/amperka/TroykaMQ
# Author: Alexey Tveritinov [kartun@yandex.ru]
from BaseMQ import BaseMQ 
from micropython import const

class MQ7(BaseMQ):
	## Clean air coefficient
	MQ7_RO_BASE = const(27.0)	
	def __init__(self, pinData, pinHeater=-1,boardResistance = 10, baseVoltage = 5.0, measuringStrategy = BaseMQ.STRATEGY_ACCURATE):
		# Call superclass to fill attributes
		super().__init__(self, pinData, pinHeater, boardResistance, baseVoltage, measuringStrategy)
		pass

	## Measure Carbon monooxide
	def readCarbonMonoxide(self):
		return self.readScaled(-0.77, 3.38)

	##  Base RO differs for every sensor family
	def getRoInCleanAir(self):
		return self.MQ7_RO_BASE	