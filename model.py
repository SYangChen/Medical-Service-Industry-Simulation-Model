from controllor import *
from setValue import *
from view import *

def generate(world, turn):
	global wolrd_cvs

	### randomly generate patient ###
	num_Patient = random.randint(15,25)
	patient_cntr = 0
	while(patient_cntr < num_Patient):
		x = random.randint(0, Hnum-1)
		y = random.randint(0, Wnum-1)
		if( world[x][y] == ' ' or world[x][y] == '+'):
			world[x][y] = 'X'
			canvas.delete(wolrd_cvs[x][y])
			patient_cntr += 1
		else:
			continue

	### randomly generate doctor every turn ###
	number_Doctor = random.randint(2, 6) # 3.76
	doctor_cntr = 0;
	while(doctor_cntr < number_Doctor):
		x = random.randint(0, Hnum-1)
		y = random.randint(0, Wnum-1)
		world[x][y] = '+'
		canvas.delete(wolrd_cvs[x][y])
		doctor_cntr += 1

	### Every turn Patient may be Self-healed ###

	heal_cntr = 0
	#number_selfhealed = random.randint(0, int(self_healing_ratio*population['patient']))
	number_selfhealed = self_healing_ratio*population['patient']
	while(heal_cntr < number_selfhealed):
		x = random.randint(0, Hnum-1)
		y = random.randint(0, Wnum-1)
		if(world[x][y] == 'X'):
			world[x][y] = ' '
			canvas.delete(wolrd_cvs[x][y])
			heal_cntr += 1

	return world

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
	global population
	### Doctor is oversupply ###
	
	if( (population['patient'] != 0) and (population['doctor'] / population['patient']) > 12 ):
		number_Doctor = random.randint(1, 3) # retire
		doctor_cntr = 0
		while(doctor_cntr < number_Doctor):
			x = random.randint(0, Wnum-1)
			y = random.randint(0, Hnum-1)
			if(world[x][y] == '+'):
				world[x][y] = ' '
				canvas.delete(wolrd_cvs[x][y])
				doctor_cntr += 1
	
	### Doctors and patients should be maintain balance
	if(ratio >= 9): # 9.289
		number_Doctor = random.randint(0, 3) # 3.76
		doctor_cntr = 0;
		while(doctor_cntr < number_Doctor):
			x = random.randint(0, Hnum-1)
			y = random.randint(0, Wnum-1)
			world[x][y] = '+'
			canvas.delete(wolrd_cvs[x][y])
			doctor_cntr += 1

	for i in range(Hnum):
		for j in range(Wnum):
	 	### count patient ###
			patient_cntr = 0
			for d in range(Eight_DIRECTION):
				_x = i + x8_ele[d]
				_y = j + y8_ele[d]
				if(not overBorder(_x,_y) and world[_x][_y] == 'X'):
					patient_cntr += 1


			### patient case ###
			if(world[i][j] == 'X'):
				patient_cntr += 1
				###  Cluster infection ###
				if(patient_cntr >= 5):
					infected = random.randint(0,3)
					for n in range(infected):
						d = random.randint(0,7); # give random direction
						if(not overBorder(i + x8_ele[d],j + y8_ele[d])):
							world[i + x8_ele[d]][j + y8_ele[d]] = 'X'; # random infection
							canvas.delete(wolrd_cvs[i + x8_ele[d]][j + y8_ele[d]])
			### Doctor case ##
			elif(world[i][j] == '+'):
				### count patient in 11 direction ###
				patient_cntr = 0
				for d in range(DIRECTION):
					_x = i + x_ele[d]
					_y = j + y_ele[d]
					if(not overBorder(_x,_y) and world[_x][_y] == 'X'):
						patient_cntr += 1

				###  Healing patient(s) ###
				for d in range(DIRECTION):
					if(not overBorder(i + x_ele[d],j + y_ele[d])):
						world[i + x_ele[d]][j + y_ele[d]] = ' ' # become normal people
						canvas.delete(wolrd_cvs[i + x_ele[d]][j + y_ele[d]])
				### doctor move ###
				pos_i, pos_j = random.randint(-1,1), random.randint(-1,1)
				if(not overBorder(i+pos_i, j+pos_j)):
					world[i][j] = ' '
					canvas.delete(wolrd_cvs[i][j])
					world[i+pos_i][j+pos_j] = '+'

				### Doctor Overworked or retired ###
				#else:
				#	world[i][j] = ' '

	return world

def overBorder(xIndex, yIndex):
	if(xIndex < 0 or xIndex >= Hnum):
		return True
	if(yIndex < 0 or yIndex >= Wnum):
		return True
	return False

def showWorld(world):

	### draw canvas ###
	x,y = 0,0
	for i in range(Hnum):
		y = d * i
		for j in range(Wnum):
			x = d * j
			#canvas.delete(wolrd_cvs[i][j])
			if(world[i][j] == ' '):
				wolrd_cvs[i][j] = canvas.create_rectangle(x, y, x+d, y+d, fill='white')
				#canvas.create_image(x, y, anchor='nw', image=normal_img)
			elif(world[i][j] == '+'):
				#canvas.create_rectangle(x, y, x+d, y+d, fill='red')
				wolrd_cvs[i][j] = canvas.create_image(x, y, anchor='nw', image=doctor_img)
			else:
				#canvas.create_rectangle(x, y, x+d, y+d, fill='blue')
				wolrd_cvs[i][j] = canvas.create_image(x, y, anchor='nw', image=infected_img)
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