from tkinter import *
import random
import time


### initialization ###

d = 10 # diameter
W = 1200;	  H = 800 # weight, height
Wnum = int(W / d);  Hnum = int(H / d)
sleep_sec = 0.001
DIRECTION = 8
x_mv = [-d, 0, d, d, d, 0, -d, -d]
y_mv = [d, d, d, 0, -d, -d, -d, 0]
x_ele = [-1, 0, 1, 1, 1, 0, -1, -1]
y_ele = [1, 1, 1, 0, -1, -1, -1, 0]
world = []
global turn

### window ###

window = Tk()
window.title('group2_project')
window.geometry(str(W)+'x'+str(H)) # '1200x800'
#window.resizable(0,0) # fixed window size

### canvas ###
canvas = Canvas(window, bg='white', height=800, width=800)
canvas.pack()

def main():

	### inpackitialize world: all people are normal ###
	world = [[' ' for j in range(Wnum)] for i in range(Hnum)]
	turn = 0

	### start life game ###
	while(True):
		world = generate(world, turn)
		world = rule(world)

		showWorld(world)
		canvas.pack()
		canvas.update()
		turn += 1
		#time.sleep(sleep_sec)

def generate(world, turn):

	### randomly generate patient ###
	num_Patient = random.randint(10,20)
	patient_cntr = 0
	while(patient_cntr < num_Patient):
		x = random.randint(0, Hnum-1)
		y = random.randint(0, Wnum-1)
		if( world[x][y] == ' ' or world[x][y] == '+'):
			world[x][y] = 'X'
			patient_cntr += 1
		else:
			continue

	### randomly generate patient every third turn ###
	if(turn % 3 == 0):
		turn = 0
		number_Doctor = random.randint(1,4) # 1~4
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

def showWorld(world):

	### draw canvas ###
	x,y = 0,0
	for i in range(Hnum):
		y = d * i
		for j in range(Wnum):
			x = d * j
			if(world[i][j] == ' '):
				canvas.create_oval(x, y, x+d, y+d, fill='white')
			elif(world[i][j] == '+'):
				canvas.create_oval(x, y, x+d, y+d, fill='red')
			else:
				canvas.create_oval(x, y, x+d, y+d, fill='blue')
		x %= W

	### show on terminal ###
	print("--"*62)
	for i in range(Hnum):
		print("|", end = "")
		for j in range(Wnum):
			print(world[i][j], end="")
		print(" |")
	print("--"*62, end = "\n")

def countPeople(world):
	normal = 0  # number of normal
	doctor = 0  # number of doctor
	patient = 0 # number of patient

	for i in range(Hnum):
		for j in world[i]:
			if(j == ' '):
				normal += 1
			elif(j == 'X'):
				patient += 1
			elif(j == '+'):
				doctor += 1

	return {'normal':normal, 'doctor':doctor, 'patient':patient}

def rule(world):
	c = countPeople(world)

	### Doctor is oversupply ###
	if( (c['patient'] != 0) and (c['doctor'] / c['patient']) > 3 ):
		number_Doctor = random.randint(1, 3) # retire
		doctor_cntr = 0
		while(doctor_cntr < number_Doctor):
			x = random.randint(0, Wnum-1)
			y = random.randint(0, Hnum-1)
			if(world[x][y] == '+'):
				world[x][y] = ' '
				doctor_cntr += 1


	for i in range(Hnum):
		for j in range(Wnum):
	 	### count patient ###
			patient_cntr = 0
			for d in range(DIRECTION):
				_x = i + x_ele[d]
				_y = j + y_ele[d]
				if(not overBorder(_x,_y) and world[_x][_y] == 'X'):
					patient_cntr += 1


			### patient or people case ###
			if(world[i][j] == 'X' or world[i][j] == ' '):
				###  Cluster infection ###
				if(patient_cntr >= 5):
					infected = random.randint(1,4)
					for n in range(infected):
						d = random.randint(0,7); # give random direction
						if(not overBorder(i + x_ele[d],j + y_ele[d])):
							world[i + x_ele[d]][j + y_ele[d]] = 'X'; # random infection

			### Doctor case ##
			else:
				###  Healing patient(s) ###
				if(patient_cntr < 6):
					for d in range(DIRECTION):
						if(not overBorder(i + x_ele[d],j + y_ele[d])):
							world[i + x_ele[d]][j + y_ele[d]] = ' ' # become normal people
					pos_i, pos_j = random.randint(-1,1), random.randint(-1,1)
					if(not overBorder(i+pos_i, j+pos_j)):
						world[i][j] = ' '
						i, j = i+pos_i, j+pos_j
						world[i][j] = '+'
				### Doctor Overworked or retired ###
				else:
					world[i][j] = ' '

	return world

def overBorder(xIndex, yIndex):
	if(xIndex < 0 or xIndex >= Hnum):
		return True
	if(yIndex < 0 or yIndex >= Wnum):
		return True
	return False

	
main()