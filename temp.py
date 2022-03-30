from m5stack import *
from m5ui import *
from uiflow import *
import unit
import machine

isDesiredTemp = False

setScreenColor(0x000000)
env20 = unit.get(unit.ENV3, unit.PORTA)


currentTemp = M5TextBox(100, 95, "Temp", lcd.FONT_DejaVu24, 0xFFFFFF, rotate=0)
isDesiredTempTextBox = M5TextBox(25, 150, "Status", lcd.FONT_DejaVu18, 0xFFFFFF, rotate=0)

pin0 = machine.Pin(1, mode=machine.Pin.OUT, pull=0x00)
pin0.off()

while True:
  myTemp = (env20.temperature * 9 / 5) + 12
  currentTemp.setText(str(myTemp))
  wait_ms(2)
  if (myTemp >= 60):
    isDesiredTemp = True
    setScreenColor(0x00FF00) 
    currentTemp = M5TextBox(100, 95, str(myTemp), lcd.FONT_DejaVu24, 0x000000, rotate=0)
    isDesiredTempTextBox = M5TextBox(40, 150, "Status", lcd.FONT_DejaVu18, 0x000000, rotate=0)
    isDesiredTempTextBox.setText("Desired Temp Reached!")
    pin0.on()
    break
  else:
    isDesiredTempTextBox.setText("Desired Temp Not Reached")
    
    