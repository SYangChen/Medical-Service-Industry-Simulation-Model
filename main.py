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
	global population

	### Infomation ###
	speed_Msg = "Speed : " + str(speed)
	normal_Msg = "Normal : " + str(population['normal'])
	doctor_Msg = "Doctor : " + str(population['doctor'])
	infected_Msg = "Infected : " + str(population['patient'])

	if(population['doctor'] != 0):
		ratio = "病人/醫生比: " + format(population['patient'] / population['doctor'], '.2f')
	else:
		ratio = "病人/醫生比: 0"

	Label(window, justify=LEFT, textvariable=speed_Msg, fg='black', font=('Arial', 12), width=15, height=2).place(x=1505,y=10)	
	Label(window, justify=LEFT, text=normal_Msg, fg='black', font=('Arial', 12), width=15, height=2).place(x=1505,y=100)
	Label(window, justify=LEFT, text=doctor_Msg, fg='black', font=('Arial', 12), width=15, height=2).place(x=1505,y=140)
	Label(window, justify=LEFT, text=infected_Msg, fg='black', font=('Arial', 12), width=15, height=2).place(x=1505,y=180)
	Label(window, justify=LEFT, text=ratio, fg='black', font=('Arial', 12), width=15, height=2).place(x=1505,y=220)


main()