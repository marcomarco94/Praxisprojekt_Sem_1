import time
import sys
import random

from rgbmatrix import RGBMatrix, RGBMatrixOptions
import lcddriver
from time import *
lcd = lcddriver.lcd()

options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.gpio_slowdown = 3

matrix = RGBMatrix(options = options)
offset_canvas = matrix.CreateFrameCanvas()



def lcd_monitor():
	lcd.lcd_clear()
	lcd.lcd_display_string(" joy-IT", 1)
	lcd.lcd_display_string("HallO Ihr!", 2)
	lcd.lcd_display_string(" I2C Serial", 3)
	lcd.lcd_display_string(" LCD", 4)

def quaderZeichnen(x, y, farbe, besetzt, amZug):
	if(farbe == 'gelb' and besetzt != 'besetzt'): 
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				offset_canvas.SetPixel(i, j, 255, 255, 0)
				if(i == x + 1 and j == y + 1):
					offset_canvas.SetPixel(i, j, 0 , 0, 0)
				else: 
					offset_canvas.SetPixel(i, j, 255, 255, 0)
	elif(farbe == 'gelb' and besetzt == 'besetzt' and amZug != 'amZug'): 
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				offset_canvas.SetPixel(i, j, 255, 255, 0)
	elif(farbe == 'gelb' and besetzt == 'besetzt' and amZug == 'amZug'): 
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				if(i == x and j == y) or (i == x and j == y + 2) or (i == x + 2 and j == y)  or (i == x + 2 and j == y + 2):
					offset_canvas.SetPixel(i, j, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
				else: 
					offset_canvas.SetPixel(i, j, 255, 255, 0)

	if(farbe == 'gruen' and besetzt != 'besetzt'): 
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				offset_canvas.SetPixel(i, j, 0, 136, 0)
				if(i == x + 1 and j == y + 1):
					offset_canvas.SetPixel(i, j, 0 , 0, 0)
				else: 
					offset_canvas.SetPixel(i, j, 0, 136, 0)
	elif(farbe == 'gruen' and besetzt == 'besetzt' and amZug != 'amZug'): 
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				offset_canvas.SetPixel(i, j, 0, 136, 0)
	elif(farbe == 'gruen' and besetzt == 'besetzt' and amZug == 'amZug'): 
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				if(i == x and j == y) or (i == x and j == y + 2) or (i == x + 2 and j == y)  or (i == x + 2 and j == y + 2):
					offset_canvas.SetPixel(i, j, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
				else: 
					offset_canvas.SetPixel(i, j, 0, 136, 0)

	if(farbe == 'blau' and besetzt != 'besetzt'): 
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				offset_canvas.SetPixel(i, j, 0, 0, 255)
				if(i == x + 1 and j == y + 1):
					offset_canvas.SetPixel(i, j, 0 , 0, 0)
				else: 
					offset_canvas.SetPixel(i, j, 0, 0, 255)
	elif(farbe == 'blau' and besetzt == 'besetzt' and amZug != 'amZug'): 
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				offset_canvas.SetPixel(i, j, 0, 0, 255)
	elif(farbe == 'blau' and besetzt == 'besetzt' and amZug == 'amZug'): 
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				if(i == x and j == y) or (i == x and j == y + 2) or (i == x + 2 and j == y)  or (i == x + 2 and j == y + 2):
					offset_canvas.SetPixel(i, j, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
				else: 
					offset_canvas.SetPixel(i, j, 0, 0, 255)

	if(farbe == 'rot' and besetzt != 'besetzt'): 
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				offset_canvas.SetPixel(i, j, 255, 0, 0)
				if(i == x + 1 and j == y + 1):
					offset_canvas.SetPixel(i, j, 0, 0, 0)
				else: 
					offset_canvas.SetPixel(i, j, 255, 0, 0)
	elif(farbe == 'rot' and besetzt == 'besetzt' and amZug != 'amZug'): 
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				offset_canvas.SetPixel(i, j, 255, 0, 0)
	elif(farbe == 'rot' and besetzt == 'besetzt' and amZug == 'amZug'): 
		for i in range(x, x + 3):
			for j in range(y, y + 3):
				if(i == x and j == y) or (i == x and j == y + 2) or (i == x + 2 and j == y)  or (i == x + 2 and j == y + 2):
					offset_canvas.SetPixel(i, j, random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
				else: 
					offset_canvas.SetPixel(i, j, 255, 0, 0)


def spielfeldZeichnen():
	#gelbes Feld links oben
	quaderZeichnen(2, 2,'gelb', 'besetzt', 'nichtAmZug')
	quaderZeichnen(2, 7,'gelb', 'besetzt', 'amZug')
	quaderZeichnen(7, 2,'gelb', 'unbesetzt', 'nichtAmZug')
	quaderZeichnen(7,7, 'gelb', 'unbesetzt', 'nichtAmZug')
	#gruenes Feld rechts oben
	quaderZeichnen(54, 2,'gruen', 'besetzt', 'amZug')
	quaderZeichnen(54, 7,'gruen', 'besetzt', 'amZug')
	quaderZeichnen(59, 2,'gruen', 'unbesetzt', 'nichtAmZug')
	quaderZeichnen(59, 7,'gruen', 'unbesetzt', 'nichtAamZug')
	#blaues Fel links unten
	quaderZeichnen(2, 54,'blau', 'besetzt', 'amZug')
	quaderZeichnen(2, 59,'blau', 'besetzt', 'amZug')
	quaderZeichnen(7, 54,'blau', 'unbesetzt', 'nichtAmZug')
	quaderZeichnen(7, 59,'blau', 'unbesetzt', 'nichtAmZug')
	#rotes Feld rechts unten
	quaderZeichnen(54, 54,'rot', 'besetzt', 'amZug')
	quaderZeichnen(54, 59,'rot', 'besetzt', 'amZug')
	quaderZeichnen(59, 54,'rot', 'unbesetzt', 'nichtAmZug')
	quaderZeichnen(59, 59,'rot' ,'unbesetzt', 'nichtAmZug')
        
while True:
    spielfeldZeichnen()
    offset_canvas = matrix.SwapOnVSync(offset_canvas)
    lcd_monitor()
    
try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
             
except KeyboardInterrupt:
    sys.exit(0)
