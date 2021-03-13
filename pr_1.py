import pygame as pg

class Circle:
    def __init__(self, x, y, rad, color):
        self.x = x
        self.y = y
        self.rad = rad
        self.color = color

    def draw(self, win):
        pg.draw.circle(win, self.color, (self.x, self.y), self.rad)

    def move_by_keys(self):
        keys = pygame.key.get_pressed()
        if keys[pg.K_a]:
            self.x -= 1
        elif keys[pg.K_d]:
            self.x += 1
        elif keys[pg.K_w]:
            self.y -= 1
        elif keys[pg.K_s]:
            self.y += 1

Red_circle = Circle(0, 0, 20, (255, 255, 0))
Red_circle.move_by_keys()
Red_circle.draw(win)