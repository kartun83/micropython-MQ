# Test for MQ-series drivers

from MQ2 import MQ2
import utime

class App:
	def __init__(self, pin = 0):
		self.sensor = MQ2(pinData = pin, baseVoltage = 3.3)

	def Run(self):
		print("Calibrating")
		self.sensor.calibrate()
		print("Calibration completed")
		print("Base resistance:{0}".format(self.sensor._ro))
		while True:
			print("Smoke: {0}".format(self.sensor.readSmoke()))
			print("LPG: {0}".format(self.sensor.readLPG()))
			print("Methane: {0}".format(self.sensor.readMethane()))
			print("Hydrogen: {0}".format(self.sensor.readHydrogen()))
			utime.sleep(5)


App().Run()			
