import pygame as pg
from constants import *
from Game.Interface.Monster_and_player_classes import Player
class EventHandler:
    pg.init()
    def __init__(self):
        pass

    def Event_L_Key(self,screen):
        font = pg.font.Font(pg.font.get_default_font(), 16)
        text = font.render("Player Attack!", True,  BLACK, WHITE)
        textrect= text.get_rect()
        textrect.center = (700,300)
        screen.blit(text, textrect)


    def monster_attack(self, player, damage):
        player.take_damage(damage)




