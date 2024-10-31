# boot.py -- run on boot-up
# run the code from main.py

import machine
import utime
import main



led = machine.Pin(2, machine.Pin.OUT)

led.on()
utime.sleep(1)
led.off()
utime.sleep(1)
print("Hello, World!")
print("tick")

print("GYRO start")
main.do()
