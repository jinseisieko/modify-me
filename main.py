import pygame as pg

from Map.map import Map
from consts import HEIGHT, WIDTH

pg.init()

screen = pg.display.set_mode((WIDTH, HEIGHT), flags=pg.NOFRAME)
clock = pg.time.Clock()
map_ = Map()

moving = False
while True:
    pressed_key = pg.key.get_pressed()
    if pressed_key[pg.K_DELETE]:
        pg.quit()
        quit()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 2 or event.button == 3:
                moving = True
        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 2 or event.button == 3:
                moving = False
    map_.update()
    map_.update_cursor(pg.mouse.get_pos(), moving)

    screen.fill(0)
    map_.draw(screen)

    pg.display.flip()
    clock.tick(120)
