import pygame as pg
class interface:
    pg.init()
    def __init__(self):
        self.width = 800
        self.height = 600
        self.white = (255, 255, 255)

    def ScreenSizing(self):
        pg.display.set_mode((self.width, self.height))
