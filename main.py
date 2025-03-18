import pygame as pg
from src import bird

def load_images():
    global game_icon, bg_image, bird_image_up, bird_image_down, bird_image_mid
    
    game_icon = pg.image.load("assets/favicon.ico")
    bg_image = pg.image.load("assets/sprites/background-day.png")
    bird_image_down = pg.image.load("assets/sprites/blue-down-bird.png")
    bird_image_up = pg.image.load("assets/sprites/blue-up-bird.png")
    bird_image_mid = pg.image.load("assets/sprites/blue-mid-bird.png")
    

# Initializing window and pygame
pg.init()
load_images()
window = pg.display.set_mode((288, 512))

# Set icon and title
pg.display.set_icon(game_icon)
pg.display.set_caption("Flappy Bird")

# Initializing bird
Flappy_bird = bird.Bird()
Flappy_bird.x = (288/2) - 17 # 17 is half of width of bird
Flappy_bird.y = (512/2) - 12 # 12 is half of height of bird

running = True

while running:
    window.blit(bg_image, (0,0))
    window.blit(bird_image_mid, (Flappy_bird.x, Flappy_bird.y))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    pg.display.update()
    