from control import *
from setValue import *

### window ###

window = Tk()
window.title('group2_project')
window.geometry('1800x1000')
#window.geometry(str(W)+'x'+str(H)) # '1200x800'
window.resizable(0,0) # fixed window size

### load image ###
normal_img = PhotoImage(file='./img/20x20/healthy.png')
infected_img = PhotoImage(file='./img/20x20/evil.png')
doctor_img = PhotoImage(file='./img/20x20/doctor-bag.png')

### canvas ###
canvas = Canvas(window, bg='white', height=H, width=W)
canvas.pack()

### button ###
speedUp_btn = Button(window, text='+', font=('Arial', 12), width=1, height=1, command=speedCtrl).place(x=1650, y=5)
speedDwon_btn = Button(window, text='-', font=('Arial', 12), width=1, height=1, command=speedCtrl).place(x=1690, y=5)

def main():

	### inpackitialize world: all people are normal ###
	world = [[' ' for j in range(Wnum)] for i in range(Hnum)]
	turn = 0

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
	role = countPeople(world)
	speed_Msg = "Speed : " + str(speed)
	normal_Msg = "Normal : " + str(role['normal'])
	doctor_Msg = "Doctor : " + str(role['doctor'])
	infected_Msg = "Infected : " + str(role['patient'])

	if(role['doctor'] != 0):
		ratio = "病人/醫生比: " + format(role['patient'] / role['doctor'], '.2f')
	else:
		ratio = "病人/醫生比: 0"
	Label(window, justify=LEFT, text=speed_Msg, fg='black', font=('Arial', 12), width=15, height=2).place(x=1505,y=10)	
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
	
main()