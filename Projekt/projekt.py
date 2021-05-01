import time
import sys
import random

from rgbmatrix import RGBMatrix, RGBMatrixOptions
import lcddriver
#from time import *
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


################################################################################################################################################################################################
################################################################################## GLOBALER ARRAY DER FELDER ###################################################################################
################################################################################################################################################################################################

alleFelderArray = (
	[1, 3, 3, "gelb"],
	[2, 3, 9, "gelb"],
	[3, 9, 3, "gelb"],
	[4, 9, 9, "gelb"],
	
	[5, 3, 51, "blau"],
	[6, 3, 57, "blau"],
	[7, 9, 51, "blau"],
	[8, 9, 57, "blau"],

	[9, 51, 3, "gruen"],
	[10, 51, 9, "gruen"],
	[11, 57, 3, "gruen"],
	[12, 57, 9, "gruen"],
	
	[13, 51, 51, "rot"],
	[14, 51, 57, "rot"],
	[15, 57, 51, "rot"],
	[16, 57, 57, "rot"],
	
	[17, 5, 25, "gelb"],
	[18, 10, 25, "weiss"],
	[19, 15, 25, "weiss"],
	[20, 20, 25, "weiss"],
	[21, 25, 25, "weiss"],
	[22, 25, 20, "weiss"],
	[23, 25, 15, "weiss"],
	[24, 25, 10, "weiss"],
	[25, 25, 5, "weiss"],
	[26, 30, 5, "weiss"],
	
	[27, 35, 5, "gruen"],
	[28, 35, 10, "weiss"],
	[29, 35, 15, "weiss"],
	[30, 35, 20, "weiss"],
	[31, 35, 25, "weiss"],
	[32, 40, 25, "weiss"],
	[33, 45, 25, "weiss"],
	[34, 50, 25, "weiss"],
	[35, 55, 25, "weiss"],
	[36, 55, 30, "weiss"],
	
	[37, 55, 35, "rot"],
	[38, 50, 35, "weiss"],
	[39, 45, 35, "weiss"],
	[40, 40, 35, "weiss"],
	[41, 35, 35, "weiss"],
	[42, 35, 40, "weiss"],
	[43, 35, 45, "weiss"],
	[44, 35, 50, "weiss"],
	[45, 35, 55, "weiss"],
	[46, 30, 55, "weiss"],
	
	[47, 25, 55, "blau"],
	[48, 25, 50, "weiss"],
	[49, 25, 45, "weiss"],
	[50, 25, 40, "weiss"],
	[51, 25, 35, "weiss"],
	[52, 20, 35, "weiss"],
	[53, 15, 35, "weiss"],
	[54, 10, 35, "weiss"],
	[55, 5, 35, "weiss"],
	[56, 5, 30, "weiss"],
	)

################################################################################################################################################################################################
################################################################################## GLOBALER ARRAY DER FELDER ###################################################################################
################################################################################################################################################################################################

wuerfelZahlenArray = (
	[2, 30, 29],
	[2, 31, 29],
	[2, 32, 29,],
	[2, 33, 29],
	[2, 29, 30],
	[2, 34, 30],
	[2, 34, 31],
	[2, 30, 32],
	[2, 31, 32],
	[2, 32, 32],
	[2, 33, 32],
	[2, 29, 33],
	[2, 29, 34],
	[2, 30, 34],
	[2, 31, 34],
	[2, 32, 34],
	[2, 33, 34],
	[2, 34, 34],
	)

################################################################################################################################################################################################

def lcd_monitor():
	lcd.lcd_clear()
	lcd.lcd_display_string(" joy-IT", 1)
	lcd.lcd_display_string("HallO Ihr!", 2)
	lcd.lcd_display_string(" I2C Serial", 3)
	lcd.lcd_display_string(" LCD", 4)

################################################################################################################################################################################################

def quaderZeichnen(x, y, farbe, aktiv):
	#bestimmung der aktuellen Farbe
	farben = ["weiss", 255, 255, 255], ["gelb", 255, 255, 0], ["blau", 0, 0, 255], ["gruen", 0, 136, 0], ["rot", 255, 0, 0]
	for i in farben:
		if (i[0] == farbe):
			r = i[1]
			g = i[2]
			b = i[3]
	#range(1,n+1) man muss also hinten immer eins mehr machen 
	for i in range(x, x+4):
		for j in range(y, y+4):
			#Normale Farben, ohne Umrandung
			if(aktiv == 0): 
				offset_canvas.SetPixel(i, j, r, g, b)	
			#Blinkende Farben, mit Umrandung
			elif(aktiv == 1): 
				if(i==x+1 and j==y) or (i==x+2 and j==y) or (i==x and j==y+1) or (i==x and j==y+2) or (i==x+1 and j==y+3) or (i==x+2 and j==y+3) or (i==x+3 and j==y+1) or (i==x+3 and j==y+2):
					offset_canvas.SetPixel(i, j, random.randint(0, 255), 0, random.randint(0, 255))
				else:
					offset_canvas.SetPixel(i, j, r, g, b)

################################################################################################################################################################################################				
					
def wuerfelRahmen():
	#wuerfel Raender
	for i in range(28, 36):
		for j in range(28, 36):
			if (i == 28 and j in range(29, 35)) or (i == 35 and j in range(29, 35)) or (j == 28 and i in range(29, 35)) or (j == 35 and i in range(29, 35)):
				offset_canvas.SetPixel(i, j, random.randint(0, 255), 0, random.randint(0, 255))

################################################################################################################################################################################################
############################################################################################# MAIN #############################################################################################
################################################################################################################################################################################################


def main():
	print "Hello World!" 
	print "test 2"
	
	for i in alleFelderArray:
		quaderZeichnen(i[1], i[2], i[3], 0)

	#geworfene Zahl zeigen, einmalig aber ohne blinken
	for w in wuerfelZahlenArray:
		if(w[0] == 2): 
			#offset_canvas.SetPixel(w[1], w[2], random.randint(0, 255), 0, random.randint(0, 255))
			offset_canvas.SetPixel(w[1], w[2], 255, 255, 255)
	


################################################################################################################################################################################################

# Main Aufruf nur 1x und KEIN LOOP
if __name__ == "__main__":
    main()
    
# ENDLOS LOOP ULTRA SCHNELL
while True:
	#aktuelles Feld auf 17 setzen und TESTEN das es blinkt
	for i in alleFelderArray:
		if(i[0] == 17): 
			quaderZeichnen(i[1], i[2], i[3], 1)
	#wurfelRahmen zeichnen und soll auch Blinken immer
	wuerfelRahmen()
	offset_canvas = matrix.SwapOnVSync(offset_canvas) 




