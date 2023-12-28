from consts import WIDTH_MAP, CHUNK_SIZE, HEIGHT_MAP, WIDTH, HEIGHT
import pygame as pg


class Map:
    def __init__(self):
        self.field = [[None] * WIDTH_MAP for _ in range(HEIGHT_MAP)]
        self.cursor = [0., 0.]
        self.surface = pg.Surface((WIDTH_MAP * CHUNK_SIZE, HEIGHT_MAP * CHUNK_SIZE))
        self.background_surface = pg.Surface((WIDTH_MAP * CHUNK_SIZE, HEIGHT_MAP * CHUNK_SIZE))

        self._last_mouse_position_ = None
        self._init_background_surface_()

    def _init_background_surface_(self):
        self.background_surface.fill("white")

    def draw(self, screen):
        screen.blit(self.surface, (0, 0), (*self.cursor, WIDTH, HEIGHT))

    def update_cursor(self, mouse_position, activated):
        if self._last_mouse_position_ is None:
            self._last_mouse_position_ = mouse_position
        if mouse_position != self._last_mouse_position_:
            if activated:
                self.cursor[0] += self._last_mouse_position_[0] - mouse_position[0]
                self.cursor[1] += self._last_mouse_position_[1] - mouse_position[1]
            self._last_mouse_position_ = mouse_position

    def update(self):
        self.surface.blit(self.background_surface, (0, 0))
        for y, line in enumerate(self.field):
            for x, cell in enumerate(line):
                if cell is None:
                    pg.draw.rect(self.surface, 0, (x * CHUNK_SIZE, y * CHUNK_SIZE, CHUNK_SIZE, CHUNK_SIZE), width=1)
