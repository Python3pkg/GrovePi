#!/usr/bin/env python
#
# GrovePi Example for testing both digital and anlog reads
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://www.dexterindustries.com/forum/?forum=grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''
import time
import grovepi
 
# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
button2 = 2
button3 = 3
button4 = 4
sensor0 = 0		 
sensor1 = 1		 
sensor2 = 2	

grovepi.pinMode(button2,"INPUT")
grovepi.pinMode(button3,"INPUT")
grovepi.pinMode(button4,"INPUT")

while True:
	try:
		print(time.time(), end=' ')
		d2=grovepi.digitalRead(button2)
		d3=grovepi.digitalRead(button3)
		d4=grovepi.digitalRead(button4)
		sensor_value0 = grovepi.analogRead(sensor0)
		sensor_value1 = grovepi.analogRead(sensor1)
		sensor_value2 = grovepi.analogRead(sensor2)
		print(("%d,%d,%d" %(d2,d3,d4)), end=' ')
		print(("%d,%d,%d" %(sensor_value0,sensor_value1,sensor_value2)))
	except IOError:
		print ("Error")
