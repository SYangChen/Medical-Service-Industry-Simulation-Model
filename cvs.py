from tkinter import *
import random


### initialization ###

d = 10 # diameter
W = 1200;	  H = 800 # weight, height
Wnum = int(W / d);  Hnum = int(H / d)
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
canvas = Canvas(window, bg='black', height=800, width=800)
canvas.pack()

def main():

	### initialize world: all people are normal ###
	world = [[' ' for j in range(Hnum)] for i in range(Wnum)]
	turn = 0

	### start life game ###
	while(True):
		world = generate(world, turn)
		world = rule(world)

		showWorld(world)
		canvas.pack()
		window.mainloop()
		turn += 1

def generate(world, turn):
	### randomly generate patient ###
	num_Patient = random.randint(1,10)
	patient_cntr = 0
	while(patient_cntr < num_Patient):
		x = random.randint(0, Wnum-1)
		y = random.randint(0, Hnum-1)
		if( world[x][y] == ' ' or world[x][y] == '+'):
			world[x][y] = 'X'
			patient_cntr += 1
		else:
			continue

	### randomly generate patient every third turn ###
	if(turn % 3 == 0):
		turn = 0;
		number_Doctor = random.randint(1,4) # 1~4
		doctor_cntr = 0;
		while(doctor_cntr < number_Doctor):
			x = random.randint(0, Wnum-1)
			y = random.randint(0, Hnum-1)
			world[x][y] = '+'
			doctor_cntr += 1

	return world

def showWorld(world):
	x,y = 0,0
	for i in range(Hnum):
		for j in world[i]:
			if(j == ' '):
				canvas.create_oval(x, y, x+d, y+d, fill='white')
			elif(j == '+'):
				canvas.create_oval(x, y, x+d, y+d, fill='red')
			else:
				canvas.create_oval(x, y, x+d, y+d, fill='blue')
			x+=d
		y+=d

	canvas.pack()

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
	count = countPeople(world)

	for i in range(Wnum):
		for j in range(Hnum):
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
				if(patient_cntr < 4):
					for d in range(DIRECTION):
						if(not overBorder(i + x_ele[d],j + y_ele[d])):
							world[i + x_ele[d]][j + y_ele[d]] = ' ' # become normal people

				### Doctor Overworked or retired ###
				else:
					world[i][j] = ' '

	return world

def overBorder(xIndex, yIndex):
	if(xIndex < 0 or xIndex >= Wnum):
		return True
	if(yIndex < 0 or yIndex >= Hnum):
		return True
	return False

	
main()