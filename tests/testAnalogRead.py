"""het lezen van een analoge input"""
import asyncio
from lj_cp import u6
import math

myU6 = u6.U6()
volt = asyncio.run(myU6.getAIN(0))
print('Spanning: ',volt,'V')

Ra: float = 22000 # Resistance voltage divider (22 kOhm)
R_NTC = Ra*volt/(5.-volt)
print('Weerstand: ',R_NTC,'Ohm')

# Steinhart–Hart equation for 10KOhm NTC
A = 0.001125308852122
B = 0.000234711863267
C = 0.000000085663516
Temp = 1/(A + B*math.log(R_NTC) + C*math.log(R_NTC)**3) - 273.
print('Temp: ',Temp,'ºC')

myU6.close()
    