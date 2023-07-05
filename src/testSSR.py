"""aansturen van een solid state relais"""
import u6
import time

myU6 = u6.U6()
print(myU6)
pin_nr:int = 0 # FIO0
myU6.setDOState(pin_nr, state=0) # When the digital line is set to output-low, control current flows and the relay turns on.
time.sleep(10)
ssr_off = myU6.getDIState(pin_nr) # When the digital line is set to input, control current does not flow and the relay turns off
# print(ssr_off)

myU6.close()
