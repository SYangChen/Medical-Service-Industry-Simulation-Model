from controllor import *
from setValue import *
from view import *
from model import *

def main():

	global population, turn

	### inpackitialize world: all people are normal ###
	world = [[' ' for j in range(Wnum)] for i in range(Hnum)]

	### start life game ###
	while(True):
		world = generate(world, turn)
		population = countPeople(world)
		world = rule(world)
		printInfo(world)
		showWorld(world)
		canvas.pack()
		canvas.update()
		turn += 1
		time.sleep(1)

def printInfo(world):
	global population, color, ratio
	global speed_Msg, normal_Msg, doctor_Msg, infected_Msg, ratio_Msg

	### Infomation ###
	speed_Msg.set("Speed : " + str(speed))
	normal_Msg.set("Normal : " + str(population['normal']))
	doctor_Msg.set("Doctor : " + str(population['doctor']))
	infected_Msg.set("Infected : " + str(population['patient']))

	change = False
	if(population['doctor'] != 0):
		ratio = population['patient'] / population['doctor']
		if(ratio <= 7.0):
			if( color != 'green'):
				change = True
				color = 'green'
		elif(ratio > 7.0 and ratio <= 15.0):
			if( color != 'yellow'):
				change = True
				color = 'yellow'
		else:
			if( color != 'red'):
				color = 'red'
				change = True
			color = 'red'

		if(change):
			Label(window, textvariable=ratio_Msg, bg = color, fg='black', font=('Arial', 12), width=15, height=2).place(x=1550,y=220)

		ratio_Msg.set("病人/醫生比: " + format(ratio, '.2f'))

main()