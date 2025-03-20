import random

def calc_coords():
    return random.randint(-250, 0) # 320 is height of beam so for keeping it's head, I used -250. It's for flipped/upper beam

class Pipe:
    def __init__(self):
        self.x = 288
        self.y = 0
        
    def reset(self, pipe_width, width):
        self.x = self.x + pipe_width + width