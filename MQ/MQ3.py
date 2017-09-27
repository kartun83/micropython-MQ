#include "MQ3.h"

MQ3.MQ3(uint8_t pin)
    : BaseMQ(pin)


MQ3.MQ3(uint8_t pin, pinHeater)
    : BaseMQ(pin, pinHeater)


def readAlcoholMgL(self):
    return readScaled(-0.66, -0.62)


def readAlcoholPpm(self):
    return readScaled(-0.66, -0.62)*2.2

