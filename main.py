import pygame as pg
from src import bird
from src import pipe

def load_images():
    global game_icon, bg_image, bird_image_up, bird_image_down, bird_image_mid, pipe_image, pipe_image_flipped
    
    game_icon = pg.image.load("assets/favicon.ico")
    bg_image = pg.image.load("assets/sprites/background-day.png")
    
    bird_image_down = pg.image.load("assets/sprites/blue-down-bird.png")
    bird_image_up = pg.image.load("assets/sprites/blue-up-bird.png")
    bird_image_mid = pg.image.load("assets/sprites/blue-mid-bird.png")
    
    pipe_image = pg.image.load("assets/sprites/pipe-green.png")
    pipe_image_flipped = pg.transform.flip(pipe_image, False, True)
    

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
Flappy_bird.x = (width/2) - (bird_width/2) # 17 is half of width of bird
Flappy_bird.y = (height/2) - (bird_height/2) # 12 is half of height of bird

# Init pipe
Beam_flipped = pipe.Pipe()
Beam_flipped.y = pipe.calc_coords()
Beam = pipe.Pipe()
Beam.y = (Beam_flipped.y+pipe_height) + (bird_height*4)

# Init pipe 2
Beam_flipped_2 = pipe.Pipe()
Beam_flipped_2.x = (Beam_flipped.x) + (width/2) + (pipe_width/2)
Beam_flipped_2.y = pipe.calc_coords()

Beam_2 = pipe.Pipe()
Beam_2.x = Beam_flipped_2.x
Beam_2.y = (Beam_flipped_2.y+pipe_height) + (bird_height*4)

running = True

while running:
    # Adding the Background Image
    window.blit(bg_image, (0,0))
    # The flappy bird
    window.blit(bird_image_mid, (Flappy_bird.x, Flappy_bird.y))
    
    # First pair of pipes (flipped and straight)
    window.blit(pipe_image_flipped, (Beam_flipped.x, Beam_flipped.y))
    window.blit(pipe_image, (Beam.x, Beam.y))
    
    # Second pair of pipes
    window.blit(pipe_image_flipped, (Beam_flipped_2.x, Beam_flipped_2.y))
    window.blit(pipe_image, (Beam_2.x, Beam_2.y))
    
    # Moving the pipes
    Beam_flipped.x -= 0.1
    Beam.x -= 0.1
    Beam_flipped_2.x -= 0.1
    Beam_2.x -= 0.1
    
    # Repeating the pipes by reseting it's position
    if Beam_flipped.x < (0 - pipe_width):
        Beam_flipped.reset(pipe_width, width)
        Beam.reset(pipe_width, width)
    elif Beam_flipped_2.x < (0 - pipe_width):
        Beam_flipped_2.reset(pipe_width, width)
        Beam_2.reset(pipe_width, width)
    
    # Event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # Updating the display
    pg.display.update()
    