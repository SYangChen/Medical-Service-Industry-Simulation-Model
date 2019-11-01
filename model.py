from controllor import *
from setValue import *
from view import *

def countPeople(world):
	normal = 0  # number of normal
	doctor = 0  # number of doctor
	patient = 0 # number of patient

	for i in range(Hnum):
		for j in range(Wnum):
			if(world[i][j] == ' '):
				normal += 1
			elif(world[i][j] == 'X'):
				patient += 1
			elif(world[i][j] == '+'):
				doctor += 1

	return {'normal':normal, 'doctor':doctor, 'patient':patient}


def rule(world):
	population = countPeople(world)

	### Doctor is oversupply ###
	
	if( (population['patient'] != 0) and (population['doctor'] / population['patient']) > 3 ):
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
					infected = random.randint(0,3)
					for n in range(infected):
						d = random.randint(0,7); # give random direction
						if(not overBorder(i + x_ele[d],j + y_ele[d])):
							world[i + x_ele[d]][j + y_ele[d]] = 'X'; # random infection

			### Doctor case ##
			else:
				### count patient in 8 direction ###
				patient_cntr = 0
				for d in range(DIRECTION):
					_x = i + x_ele[d]
					_y = j + y_ele[d]
					if(not overBorder(_x,_y) and world[_x][_y] == 'X'):
						patient_cntr += 1

				###  Healing patient(s) ###
				if(patient_cntr < 6):
					for d in range(DIRECTION):
						if(not overBorder(i + x_ele[d],j + y_ele[d])):
							world[i + x_ele[d]][j + y_ele[d]] = ' ' # become normal people
					pos_i, pos_j = random.randint(-1,1), random.randint(-1,1)
					if(not overBorder(i+pos_i, j+pos_j)):
						world[i][j] = ' '
						world[i+pos_i][j+pos_j] = '+'

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