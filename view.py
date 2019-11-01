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
infected_img = PhotoImage(file='./img/20x20/evil.png')
doctor_img = PhotoImage(file='./img/20x20/doctor-bag.png')

### canvas ###
canvas = Canvas(window, bg='white', height=H, width=W)
canvas.pack()

### button ###
speedUp_btn = Button(window, text='+', font=('Arial', 12), width=1, height=1, command=speedCtrl).place(x=1650, y=5)
speedDwon_btn = Button(window, text='-', font=('Arial', 12), width=1, height=1, command=speedCtrl).place(x=1690, y=5)
