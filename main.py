from controllor import *
from setValue import *
from view import *
from model import *

def main():

	global population, turn, restart

	### inpackitialize world: all people are normal ###
	world = [[' ' for j in range(Wnum)] for i in range(Hnum)]

	### start life game ###
	while(True):
		world = generate(world, turn)
		population = countPeople(world)
		world = rule(world)

		if(turn > 10 and (ratio >= 250.0 or population['doctor'] <= 5)):
			s = "{:6} {:<6} {:<7} {:<8} {:<6}\n"
			f = open("result.txt", 'a')
			f.write(s.format(str(turn), str(population['normal']), str(population['doctor']), str(population['patient']), format(ratio, '.2f')))
			f.close()
			#restart = Label(window, text="Restart!!!", bg = 'Red', fg='white', font=('Arial', 14), width=15, height=2).place(x=1550,y=300)
			#time.sleep(5)
			#init()
			exit

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
		elif(ratio > 9.0 and ratio <= 13.0):
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