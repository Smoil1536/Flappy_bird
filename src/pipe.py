import random

def calc_coords():
    return random.randint(-250, 0) # 312 is length of beam so for keeping it's head, I used -250

class Pipe:
    x = 200
    y = 0