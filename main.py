import pygame as pg

def set_game_icon():
    game_icon = pg.image.load("assets/favicon.ico")
    pg.display.set_icon(game_icon)
    
pg.init()
window = pg.display.set_mode((600, 600))
set_game_icon()

running = True #this is a comment
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            print(event.type)
            running = False