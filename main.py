import pygame as pg

def load_images():
    global game_icon, bg_image
    
    game_icon = pg.image.load("assets/favicon.ico")
    bg_image = pg.image.load("assets/sprites/background-day.png")
    

# Initializing window and pygame
pg.init()
load_images()
window = pg.display.set_mode((288, 512))

# Set icon and title
pg.display.set_icon(game_icon)
pg.display.set_caption("Flappy Bird")

running = True

while running:
    window.blit(bg_image, (0,0))
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    pg.display.update()
    