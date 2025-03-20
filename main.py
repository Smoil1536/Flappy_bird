import pygame as pg
import random
from src import bird
from src import pipe

# Function to load assets
def load_images():
    global game_icon, bg_image, bird_image_up, bird_image_down, bird_image_mid, pipe_image, pipe_image_flipped
    
    game_icon = pg.image.load("assets/favicon.ico")
    bg_image = pg.image.load("assets/sprites/background-day.png")
    
    bird_image_down = pg.image.load("assets/sprites/blue-down-bird.png")
    bird_image_up = pg.image.load("assets/sprites/blue-up-bird.png")
    bird_image_mid = pg.image.load("assets/sprites/blue-mid-bird.png")
    
    pipe_image = pg.image.load("assets/sprites/pipe-green.png")
    pipe_image_flipped = pg.transform.flip(pipe_image, False, True)
    
def randomize_pipes():
    upY = pipe.calc_coords()
    downY = (upY+pipe_height) + (bird_height*4)
    return upY, downY

def reset_pipes(Beam_flipped, Beam):
    Beam_flipped.reset(pipe_width, width)
    Beam.reset(pipe_width, width)
    Beam_flipped.y, Beam.y = randomize_pipes()
    
    return Beam_flipped, Beam

def crash(*pipes):
    for coord, mask in pipes:
        if Flappy_bird_mask.overlap(mask, (coord.x-Flappy_bird.x, coord.y-Flappy_bird.y)):
            return True    
    if Flappy_bird.y >= height:
        return True
    return False

def move_pipes():
    Beam_flipped.x -= 0.1
    Beam.x -= 0.1
    Beam_flipped_2.x -= 0.1
    Beam_2.x -= 0.1
    
def show_pipes(flipped, straight):
    window.blit(pipe_image_flipped, (flipped.x, flipped.y))
    window.blit(pipe_image, (straight.x, straight.y))
    
# Initializing window and pygame
pg.init()
load_images()

width = bg_image.get_size()[0]
height = bg_image.get_size()[1]

pipe_width = pipe_image.get_size()[0]
pipe_height = pipe_image.get_size()[1]

bird_width = bird_image_mid.get_size()[0]
bird_height = bird_image_mid.get_size()[1]
window = pg.display.set_mode(bg_image.get_size())

# Set icon and title
pg.display.set_icon(game_icon)
pg.display.set_caption("Flappy Bird")

# Initializing bird
Flappy_bird = bird.Bird()
Flappy_bird.x = (width/2) - (bird_width/2)
Flappy_bird.y = (height/2) - (bird_height/2)

# Bird mask
Flappy_bird_mask = pg.mask.from_surface(bird_image_mid)

# Beam mask
Beam_flipped_mask = pg.mask.from_surface(pipe_image_flipped)
Beam_mask = pg.mask.from_surface(pipe_image)

# Init pipe
Beam_flipped = pipe.Pipe()
Beam = pipe.Pipe()
Beam_flipped.y, Beam.y = randomize_pipes()

# Init pipe 2
Beam_flipped_2 = pipe.Pipe()
Beam_flipped_2.x = (Beam_flipped.x) + (width/2) + (pipe_width/2)
Beam_2 = pipe.Pipe()
Beam_2.x = Beam_flipped_2.x

Beam_flipped_2.y, Beam_2.y = randomize_pipes()

running = True

while running:
    # Adding the Background Image
    window.blit(bg_image, (0,0))
    # The flappy bird
    window.blit(random.choice([bird_image_down, bird_image_mid, bird_image_up]), (Flappy_bird.x, Flappy_bird.y))
    
    # Displaying the pipes
    show_pipes(Beam_flipped, Beam)
    show_pipes(Beam_flipped_2, Beam_2)
    
    # Moving the pipes
    move_pipes()
    
    # Move flappy bird down
    Flappy_bird.y += 0.3
    
    # Collison
    if crash((Beam_flipped, Beam_flipped_mask), (Beam_flipped_2, Beam_flipped_mask), (Beam, Beam_mask), (Beam_2, Beam_mask)):
        running = False
    
    # Repeating the pipes by reseting it's position
    if Beam_flipped.x < (0 - pipe_width):
        (Beam_flipped, Beam) = reset_pipes(Beam_flipped, Beam)
    elif Beam_flipped_2.x < (0 - pipe_width):
        (Beam_flipped_2, Beam_2) = reset_pipes(Beam_flipped_2, Beam_2)
    
    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            print("yes clicked")
            print(Flappy_bird.y)
            Flappy_bird.y -= 50
    
    # Updating the display
    pg.display.update()