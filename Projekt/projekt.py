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
	[ 1,  1,  1, "gelb"],
	[ 2,  1,  7, "gelb"],
	[ 3,  7,  1, "gelb"],
	[ 4,  7,  7, "gelb"],
	
	[ 5, 53,  1, "gruen"],
	[ 6, 53,  7, "gruen"],
	[ 7, 59,  1, "gruen"],
	[ 8, 59,  7, "gruen"],
	
	[ 9, 53, 53, "rot"],
	[10, 53, 59, "rot"],
	[11, 59, 53, "rot"],
	[12, 59, 59, "rot"],
	
	[13,  1, 53, "blau"],
	[14,  1, 59, "blau"],
	[15,  7, 53, "blau"],
	[16,  7, 59, "blau"],
	
	[17,  5, 25, "gelb"],
	[18, 10, 25, "weiss"],
	[19, 15, 25, "weiss"],
	[20, 20, 25, "weiss"],
	[21, 25, 25, "weiss"],
	[22, 25, 20, "weiss"],
	[23, 25, 15, "weiss"],
	[24, 25, 10, "weiss"],
	[25, 25,  5, "weiss"],
	[26, 30,  5, "weiss"],
	
	[27, 35,  5, "gruen"],
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
	[55,  5, 35, "weiss"],
	[56,  5, 30, "weiss"],
	
	[57, 10, 30, "gelb"],
	[58, 15, 30, "gelb"],
	[59, 20, 30, "gelb"],
	[60, 25, 30, "gelb"],
	
	[61, 30, 10, "gruen"],
	[62, 30, 15, "gruen"],
	[63, 30, 20, "gruen"],
	[64, 30, 25, "gruen"],

	[65, 50, 30, "rot"],
	[66, 45, 30, "rot"],
	[67, 40, 30, "rot"],
	[68, 35, 30, "rot"],
	
	[69, 30, 50, "blau"],
	[70, 30, 45, "blau"],
	[71, 30, 40, "blau"],
	[72, 30, 35, "blau"]
	)

################################################################################################################################################################################################
################################################################################## GLOBALER ARRAY DER FELDER ###################################################################################
################################################################################################################################################################################################

wuerfelZahlenOffsetArray = (
	[1, 4, 4],
	[1, 4, 5],
	[1, 5, 4],
	[1, 5, 5],
	
	[2, 2, 2],
	[2, 2, 3],
	[2, 3, 2],
	[2, 3, 3],
	[2, 6, 6],
	[2, 6, 7],
	[2, 7, 6],
	[2, 7, 7],
	
	[3, 1, 1],
	[3, 1, 2],
	[3, 2, 1],
	[3, 2, 2],
	[3, 4, 4],
	[3, 4, 5],
	[3, 5, 4],
	[3, 5, 5],
	[3, 7, 7],
	[3, 7, 8],
	[3, 8, 7],
	[3, 8, 8],
	
	[4, 2, 2],
	[4, 2, 3],
	[4, 3, 2],
	[4, 3, 3],
	[4, 6, 6],
	[4, 6, 7],
	[4, 7, 6],
	[4, 7, 7],
	[4, 2, 6],
	[4, 2, 7],
	[4, 3, 6],
	[4, 3, 7],
	[4, 6, 2],
	[4, 6, 3],
	[4, 7, 2],
	[4, 7, 3],
	
	[5, 1, 1],
	[5, 1, 2],
	[5, 2, 1],
	[5, 2, 2],
	[5, 7, 7],
	[5, 7, 8],
	[5, 8, 7],
	[5, 8, 8],
	[5, 4, 4],
	[5, 4, 5],
	[5, 5, 4],
	[5, 5, 5],
	[5, 1, 7],
	[5, 1, 8],
	[5, 2, 7],
	[5, 2, 8],
	[5, 7, 1],
	[5, 7, 2],
	[5, 8, 1],
	[5, 8, 2],
	

	[6, 2, 1],
	[6, 3, 1],
	[6, 6, 1],
	[6, 7, 1],
	[6, 2, 2],
	[6, 3, 2],
	[6, 6, 2],
	[6, 7, 2],
	[6, 2, 4],
	[6, 3, 4],
	[6, 6, 4],
	[6, 7, 4],
	[6, 2, 5],
	[6, 3, 5],
	[6, 6, 5],
	[6, 7, 5],
	[6, 2, 7],
	[6, 3, 7],
	[6, 6, 7],
	[6, 7, 7],
	[6, 2, 8],
	[6, 3, 8],
	[6, 6, 8],
	[6, 7, 8]
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
					
def wuerfelRahmen(xOffset, yOffset):
	#wuerfel Raender
	for i in range(xOffset, xOffset+12):
		for j in range(yOffset, yOffset+12):
			if (i == xOffset and j in range(yOffset, yOffset+12)) or (i == xOffset+11 and j in range(yOffset, yOffset+12)) or (j == yOffset and i in range(xOffset, xOffset+12)) or (j == yOffset+11 and i in range(xOffset, xOffset+12)):
				offset_canvas.SetPixel(i, j, random.randint(0, 255), 0, random.randint(0, 255))
			else:
				offset_canvas.SetPixel(i, j, 0, 0, 0)

################################################################################################################################################################################################	
				
def wuerfelZahlen(xOffset, yOffset, zahl):
	#geworfene Zahl zeigen
	for w in wuerfelZahlenOffsetArray:
			if(w[0] == zahl): 
				#offset_canvas.SetPixel(xOffset+1+w[1], yOffset+1+w[2], random.randint(0, 255), 0, random.randint(0, 255))
				offset_canvas.SetPixel(xOffset+1+w[1], yOffset+1+w[2], 255, 255, 255)
				
################################################################################################################################################################################################
############################################################################################# MAIN #############################################################################################
################################################################################################################################################################################################


def main():
	print "Hello World!" 
	print "test 2"
	
	for i in alleFelderArray:
		quaderZeichnen(i[1], i[2], i[3], 0)



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
	wuerfelRahmen(12, 12)
	wuerfelZahlen(12, 12, 2)
	
	wuerfelRahmen(40, 12)
	wuerfelZahlen(40, 12, 3)
	
	wuerfelRahmen(12, 40)
	wuerfelZahlen(12, 40, 4)
	
	wuerfelRahmen(40, 40)
	wuerfelZahlen(40, 40, 5)
	

	offset_canvas = matrix.SwapOnVSync(offset_canvas) 




