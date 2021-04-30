import time
import sys

from rgbmatrix import RGBMatrix, RGBMatrixOptions


options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'regular'  # If you have an Adafruit HAT: 'adafruit-hat'
options.gpio_slowdown = 3

matrix = RGBMatrix(options = options)
offset_canvas = matrix.CreateFrameCanvas()

def quaderZeichnen(x, y, rgb1, rgb2, rgb3, farbe, besetzt, amZug):
    for i in range(x, x + 3):
        offset_canvas.SetPixel(i, y, rgb1, rgb2, rgb3)
    	for j in range(y + 1, y + 3):
			offset_canvas.SetPixel(i, j, rgb1, rgb2, rgb3)

def spielfeldZeichnen():
	#gelbes Feld links oben
	quaderZeichnen(2, 2, 255, 255, 0, gelb, besetzt, nichtAmZug)
	quaderZeichnen(2, 7, 255, 255, 0, gelb. besetzt, amZug)
	quaderZeichnen(7, 2, 255, 255, 0, gelb, unbesetzt, amZug)
	quaderZeichnen(7, 7, 255, 255, 0, gelb, unbesetzt, amZug)
	#gruenes Fel rechts oben
	quaderZeichnen(54, 2, 0, 136, 0, grün, besetzt, amZug)
	quaderZeichnen(54, 7, 0, 136, 0, grün, besetzt, amZug)
	quaderZeichnen(59, 2, 0, 136, 0, grün, unbesetzt, amZug)
	quaderZeichnen(59, 7, 0, 136, 0, grün, unbesetzt, amZug)
	#blaues Fel links unten
	quaderZeichnen(2, 54, 0, 0, 255, blau, besetzt, amZug)
	quaderZeichnen(2, 59, 0, 0, 255, blau, besetzt, amZug)
	quaderZeichnen(7, 54, 0, 0, 255, blau, unbesetzt, amZug)
	quaderZeichnen(7, 59, 0, 0, 255, blau, unbesetzt, amZug)
	#rotes Feld rechts unten
	quaderZeichnen(54, 54, 255, 0, 0, rote, besetzt, amZug)
	quaderZeichnen(54, 59, 255, 0, 0, rote, besetzt, amZug)
	quaderZeichnen(59, 54, 255, 0, 0, rote, unbesetzt, amZug)
	quaderZeichnen(59, 59, 255, 0, 0, rote ,unbesetzt, amZug)
        
while True:
    spielfeldZeichnen()	
    offset_canvas = matrix.SwapOnVSync(offset_canvas)      
	

try:
    print("Press CTRL-C to stop.")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    sys.exit(0)
