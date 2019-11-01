### initialization ###

d = 20 # rectangle size
W, H = 1200, 800; # weight, height
Wnum, Hnum = int(W / d), int(H / d)

speed = 1  # 1~10
sleep_sec = 1 / (5 * 0.1* speed)
hit = False

DIRECTION = 8
x_ele = [-1, 0, 1, 1, 1, 0, -1, -1]
y_ele = [1, 1, 1, 0, -1, -1, -1, 0]

world = []
turn = 0

population = {'normal':0, 'doctor':0, 'patient':0}
ratio = 0 # 病人/醫生比