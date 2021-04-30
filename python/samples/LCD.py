import lcddriver
from time import *
lcd = lcddriver.lcd()

try:
	while True:
		lcd.lcd_clear()
		lcd.lcd_display_string(" joy-IT", 1)
		lcd.lcd_display_string("HallO!", 2)
		lcd.lcd_display_string(" I2C Serial", 3)
		lcd.lcd_display_string(" LCD", 4)

		sleep(100)

except KeyboardInterrupt:
	lcd.lcd_clear()
