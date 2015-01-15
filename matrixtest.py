#!/usr/bin/python

import time
from rgbmatrix import Adafruit_RGBmatrix

# Rows and chain length are both required parameters:
matrix = Adafruit_RGBmatrix(32, 1)

# Flash screen red, green, blue (packed color values)
#matrix.Fill(0xFF0000)
#time.sleep(1.0)
#matrix.Fill(0x00FF00)
#time.sleep(1.0)
#matrix.Fill(0x0000FF)
#time.sleep(1.0)

# Show RGB test pattern (separate R, G, B color values)
for b in range(16):
	for g in range(8):
		for r in range(8):
			matrix.SetPixel(
			  (b / 4) * 8 + g,
			  (b & 3) * 8 + r,
			  (r * 0b001001001) / 2,
			  (g * 0b001001001) / 2,
 			   b * 0b00010001)

time.sleep(10.0)
matrix.Clear()
