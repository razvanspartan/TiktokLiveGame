import pygame as pg
from Game.Event_Handler.EventHandler import EventHandler
from constants import *
from Game.Interface.Monster_and_player_classes import Player
class GameWindow:
    pg.init()
    def __init__(self):
        self.events = EventHandler()
        self.run = True
        self.width = 800
        self.height = 600
        self.screen = pg.display.set_mode((self.width,self.height))
        player_image = pg.image.load('images/player.png')
        self.playerVisual = pg.transform.smoothscale(player_image,(200,200))
        self.player=Player(1,50,100, self.playerVisual)
        self.Monster_attack_event=pg.USEREVENT+1
        pg.time.set_timer(self.Monster_attack_event,10000)

    def draw_health_rectangle(self, screen, x, y, health):
        if health < 0:
            health = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 20
        fill = (health / 100) * BAR_LENGTH
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
        pg.draw.rect(screen, RED, fill_rect)
        pg.draw.rect(screen, BLACK, outline_rect, 2)

    def run_game(self):
        while self.run:
            pg.time.delay(100)
            self.screen.fill((255,255,255))
            self.draw_health_rectangle(self.screen, 650, 500, self.player.health_current)
            key = pg.key.get_pressed()
            if key[pg.K_l]:
                self.events.Event_L_Key(self.screen)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                    pg.quit()
                elif event.type == self.Monster_attack_event:
                    self.events.monster_attack(self.player, 5)
            self.screen.blit(self.player.image,(600,300))
            pg.display.update()
