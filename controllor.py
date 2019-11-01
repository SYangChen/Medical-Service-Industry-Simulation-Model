from tkinter import *
from setValue import *
import random
import time

def speedCtrl():
	global hit, speed
	if hit == False:
		hit = True
		speed += 1
		#var.set('10')
	else:
		hit = False
		#var.set('')