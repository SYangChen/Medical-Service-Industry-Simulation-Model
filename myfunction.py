from tkinter import *
import random
import time

hit = False
def speedCtrl():
	global hit
	if hit == False:
		hit = True
		speed += 1
		#var.set('10')
	else:
		hit = False
		#var.set('')