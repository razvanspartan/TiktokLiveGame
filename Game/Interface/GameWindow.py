import pygame as pg
from Game.Event_Handler.EventHandler import EventHandler
from constants import *
from Game.Interface.Monster_and_player_classes import *
class GameWindow:
    path = "..\Game\events.txt"
    fileopen=open(path,"r")
    pg.init()
    def __init__(self):
        self.events = EventHandler()
        self.run = True
        self.width = 800
        self.height = 600
        self.screen = pg.display.set_mode((self.width,self.height))

        player_image = pg.image.load('images/player.png')
        self.playerVisual = pg.transform.smoothscale(player_image,(200,200))
        self.player=Player(1,50,100, self.playerVisual,1)

        self.Monster_attack_event=pg.USEREVENT+1
        pg.time.set_timer(self.Monster_attack_event,10000)
        monster1_image = pg.image.load('images/Monster1.png')
        self.monster1Visual = pg.transform.smoothscale(monster1_image,(150,150))
        self.monster=Monster1(50,100,100, self.monster1Visual)
        path = "..\Game\events.txt"
        self.fileopen=open(path,"r")

    def Game_Over_scene(self):
        SceneContinue=True
        time=5000
        while SceneContinue:
            self.monster.attack=0
            time-=1
            if time==0:
                SceneContinue=False
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                    pg.quit()
            self.screen.fill((255,255,255))
            game_over = pg.font.Font(None, 36)
            text = game_over.render('Game Over', True, BLACK)
            self.screen.blit(text, (400, 300))
            pg.display.update()
        return
    def draw_stat_rectangle(self):
        '''This function draws the player's health and attack on the screen.'''
        pg.draw.rect(self.screen, WHITE, (10,470,180,180))
        pg.draw.rect(self.screen, BLACK, (0, 450, 500, 200), 2)
    def draw_stat_bar(self,player):
        '''This function draws the player's health and attack on the screen. It takes in the player object.'''
        font = pg.font.Font(None, 36)
        health_text = font.render(f'Health: {player.health_current}/{player.health_max}', True, BLACK)
        attack_text = font.render(f'Attack: {player.attack}', True, BLACK)
        level_text = font.render(f'Level: {player.level}', True, BLACK)
        self.screen.blit(level_text, (10, 460))
        self.screen.blit(health_text, (10, 500))
        self.screen.blit(attack_text, (10, 540))

    def draw_monster_health(self, screen, monster):
        '''This function draws the monster health on the screen. It takes in the screen and the monster object.'''
        self.draw_health_rectangle(screen, 125, 75, monster.health_current)
    def draw_monster(self, screen, monster):
        '''This function draws the monster on the screen. It takes in the screen and the monster object.'''
        screen.blit(monster.image, (100, 100))

    '''This function draws the health bar on the screen. It takes in the screen, the x and y coordinates of the health bar,'''
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

    '''This function runs the game and updates the screen. It also checks for events 
    such as the monster attack event and the quit event. It also checks for the like press event.'''
    def run_game(self, giftlist):
        pg.mixer_music.load('images/soundtrack.mp3')
        pg.mixer_music.play(-1)
        while self.run:
            pg.time.delay(100)

            self.screen.fill((255,255,255))
            self.draw_stat_rectangle()
-
            self.draw_health_rectangle(self.screen, 650, 500, self.player.health_current)
            self.draw_monster(self.screen, self.monster)
            self.draw_monster_health(self.screen, self.monster)
            self.draw_stat_bar(self.player)
            if self.player.health_current <= 0:
                self.Game_Over_scene()
                self.player=Player(1,200,100, self.playerVisual,1)
                self.monster=Monster1(50,100,100, self.monster1Visual)
            command = self.fileopen.readline()
            if command == "like \n":
                self.events.Event_L_Key(self.screen,self.monster,self.player)
            elif key[pg.K_r]:
                self.player.health_current = self.player.health_current + 5
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                    pg.quit()
                elif event.type == self.Monster_attack_event:
                    self.events.monster_attack(self.player, self.monster)
            self.screen.blit(self.player.image,(600,300))
            pg.display.update()
