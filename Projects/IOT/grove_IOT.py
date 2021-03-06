'''
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

import xively
import datetime
import sys
import time
import grovepi

sensor = 4

XIVELY_API_KEY = "xmvAR7Y2KxAd00B8AFS1smKCsMigYheWFCybsx58sc2DmFOJ"
XIVELY_FEED_ID = "631205699"

api = xively.XivelyAPIClient(XIVELY_API_KEY)
feed = api.feeds.get(XIVELY_FEED_ID)

while True:
	try:
		now = datetime.datetime.utcnow()

		[temp,humidity] = grovepi.dht(sensor,1)
		light=int(grovepi.analogRead(0)/10.24)
		sound=int(grovepi.analogRead(1)/10.24)
		
		print((temp,humidity,light,sound))
		
		feed.datastreams = [
			xively.Datastream(id='temp', current_value=temp, at=now),
			xively.Datastream(id='humidity', current_value=humidity, at=now),
			xively.Datastream(id='light', current_value=light, at=now),
			xively.Datastream(id='sound', current_value=sound, at=now),
		]
		feed.update()
		time.sleep(10)
	except:
		print("Error")