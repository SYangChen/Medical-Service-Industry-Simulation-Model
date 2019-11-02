### initialization ###

d = 20 # rectangle size
W, H = 1200, 800; # weight, height
Wnum, Hnum = int(W / d), int(H / d)

speed = 10000  # 1~10
sleep_sec = 1 / (100 * speed)
hit = False


Eight_DIRECTION = 8
x8_ele = [-1, 0, 1, 1, 1, 0,-1,-1]
y8_ele = [ 1, 1, 1, 0,-1,-1,-1, 0]

DIRECTION = 12
x_ele = [-1, 0, 0, 1, 1, 2, 1, 0, 0,-1,-1,-2]
y_ele = [ 1, 1, 2, 1, 0, 0,-1,-1,-2,-1, 0, 0]

world = []
turn = 0

population = {'normal':0, 'doctor':0, 'patient':0}
ratio = 1 # patient / doctor

### probability ###
self_healing_ratio = 0.4