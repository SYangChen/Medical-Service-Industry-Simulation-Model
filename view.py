from tkinter import *
from setValue import *
from controllor import *

### window ###

window = Tk()
window.title('group2_project')
window.geometry('1800x1000')
#window.geometry(str(W)+'x'+str(H)) # '1200x800'
window.resizable(0,0) # fixed window size

### load image ###
normal_img = PhotoImage(file='./img/20x20/healthy.png')
infected_img = PhotoImage(file='./img/20x20/spooky1.png')
doctor_img = PhotoImage(file='./img/20x20/doctor-bag.png')

### canvas ###
canvas = Canvas(window, bg='white', height=H, width=W)
canvas.pack()

### button ###
"""
speedUp_btn = Button(window, text='+', font=('Arial', 12), width=1, height=1, command=speedCtrl).place(x=1650, y=5)
speedDwon_btn = Button(window, text='-', font=('Arial', 12), width=1, height=1, command=speedCtrl).place(x=1690, y=5)
"""

### Infomation Lable ###
speed_Msg = StringVar()
normal_Msg = StringVar()
doctor_Msg = StringVar()
infected_Msg = StringVar()
ratio_Msg = StringVar()

speed_Msg.set("Speed : " + str(speed))
normal_Msg.set("Normal : " + str(population['normal']))
doctor_Msg.set("Doctor : " + str(population['doctor']))
infected_Msg.set("Infected : " + str(population['patient']))
ratio_Msg.set("病人/醫生比: 0")

color = 'green' # Label mark: green = normal, yellow = warning, red = danger

Label(window, textvariable=speed_Msg, fg='black', font=('Arial', 12), width=15, height=2).place(x=1550,y=10)	
Label(window, text="***Infomation***", bg = 'black', fg='white', font=('Arial', 14), width=15, height=2).place(x=1545,y=50)
Label(window, textvariable=normal_Msg, fg='black', font=('Arial', 12), width=15, height=2).place(x=1550,y=100)
Label(window, textvariable=doctor_Msg, fg='black', font=('Arial', 12), width=15, height=2).place(x=1550,y=140)
Label(window, textvariable=infected_Msg, fg='black', font=('Arial', 12), width=15, height=2).place(x=1550,y=180)
Label(window, textvariable=ratio_Msg, bg = color, fg='black', font=('Arial', 12), width=15, height=2).place(x=1550,y=220)