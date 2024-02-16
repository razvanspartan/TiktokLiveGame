import pygame as pg
from constants import *
from Game.Interface.Monster_and_player_classes import *
class EventHandler:
    pg.init()
    def __init__(self):
        pass

    '''Event for liking the live on tiktok, creates a text above the player's heads'''
    def Event_L_Key(self,screen,monster,player):
        font = pg.font.Font(pg.font.get_default_font(), 16)
        text = font.render("Player Attack!", True,  BLACK, WHITE)
        textrect= text.get_rect()
        textrect.center = (700,300)
        screen.blit(text, textrect)
        monster.take_damage(player.attack)

    '''Event for the timerevent being done and attacking the player'''
    def monster_attack(self, player, monster):
        player.take_damage(monster.attack)




