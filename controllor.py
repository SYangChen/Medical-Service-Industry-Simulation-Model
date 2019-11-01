from setValue import *
import random
import time

def speedCtrl():
	global hit, speed
	if hit == False:
		hit = True
		speed += 1
		speed_Msg.set("Speed : " + str(speed))
	else:
		hit = False
		speed -= 1
		speed_Msg.set("Speed : " + str(speed))