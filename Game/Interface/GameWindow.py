import pygame as pg
from Game.Interface.interface import interface
from Game.Event_Handler.EventHandler import EventHandler

class GameWindow:
    pg.init()
    def __init__(self):
        self.events = EventHandler()
        self.interface = interface()
        self.run = True
        self.interface.ScreenSizing()

    def run_game(self):
        while self.run:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
            pg.display.update()
        pg.quit()
