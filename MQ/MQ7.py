#include "MQ7.h"
# Ported from https://github.com/amperka/TroykaMQ
# Author: Alexey Tveritinov [kartun@yandex.ru]

""" Clean air coefficient """
MQ7_RO_BASE = const(27.0)

class MQ2(BaseMQ):
	def __init__(self, pinData, pinHeater=-1,boardResistance = 10, baseVoltage = 5.0):
		# Call superclass to fill attributes
		super().__init__(self, pinData, pinHeater, boardResistance, baseVoltage)
		pass

	def readCarbonMonoxide(self):
		return self.readScaled(-0.77, 3.38)

	def getRoInCleanAir(self):
		return MQ7_RO_BASE	