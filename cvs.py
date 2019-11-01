from controllor import *
from setValue import *
from view import *
from model import *


def main():

	global turn

	### inpackitialize world: all people are normal ###
	world = [[' ' for j in range(Wnum)] for i in range(Hnum)]


	### start life game ###
	while(True):
		printInfo(world)
		world = generate(world, turn)
		world = rule(world)
		showWorld(world)
		canvas.pack()
		canvas.update()
		turn += 1
		time.sleep(1)

def generate(world, turn):

	### randomly generate patient ###
	num_Patient = random.randint(5,20)
	patient_cntr = 0
	while(patient_cntr < num_Patient):
		x = random.randint(0, Hnum-1)
		y = random.randint(0, Wnum-1)
		if( world[x][y] == ' ' or world[x][y] == '+'):
			world[x][y] = 'X'
			patient_cntr += 1
		else:
			continue

	### randomly generate doctor every third turn ###
	if(turn % 2 == 0):
		turn = 0
		number_Doctor = random.randint(1, 5)
		doctor_cntr = 0;
		while(doctor_cntr < number_Doctor):
			x = random.randint(0, Hnum-1)
			y = random.randint(0, Wnum-1)
			world[x][y] = '+'
			doctor_cntr += 1

	### Every turn Patient may be Self-healed ###
	heal_cntr = 0
	number_selfhealed = random.randint(1, 4)
	while(heal_cntr < number_selfhealed):
		x = random.randint(0, Hnum-1)
		y = random.randint(0, Wnum-1)
		if(world[x][y] == 'X'):
			world[x][y] = ' '
			heal_cntr += 1

	return world

def printInfo(world):
	population = countPeople(world)

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

def showWorld(world):

	### draw canvas ###
	x,y = 0,0
	for i in range(Hnum):
		y = d * i
		for j in range(Wnum):
			x = d * j
			if(world[i][j] == ' '):
				canvas.create_rectangle(x, y, x+d, y+d, fill='white')
				#canvas.create_image(x, y, anchor='nw', image=normal_img)
			elif(world[i][j] == '+'):
				#canvas.create_rectangle(x, y, x+d, y+d, fill='red')
				canvas.create_image(x, y, anchor='nw', image=doctor_img)
			else:
				#canvas.create_rectangle(x, y, x+d, y+d, fill='blue')
				canvas.create_image(x, y, anchor='nw', image=infected_img)
		x %= W

	### show on terminal ###
	"""
	print("--"*62)
	for i in range(Hnum):
		print("|", end = "")
		for j in range(Wnum):
			print(world[i][j], end="")
		print(" |")
	print("--"*62, end = "\n")
	"""

	
main()