import sys
import pygame
import random
from src import bearcat
from src import bear
from src import gator
from src import gamecock

class Controller:
    def __init__(self):
        self.width = 1000
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background_pic = "assets/background2.jpg"
        self.arena = "assets/arena.png"
        self.state = "BEGIN"
        self.run = True
        self.white = (255,255,255)
        self.p1 = None
        self.p2 = None


    def mainLoop(self):
        while self.run:
            if self.state == "BEGIN":
                self.gameIntroScreen()
            elif self.state == "GAME":
                self.gameLoop()
            elif self.state == "LOSE":
                self.gameOverScreen()
    def gameIntroScreen(self):
        #Sound
        pygame.mixer.init()
        sound = pygame.mixer.Sound("assets/song.mp3")
        sound.set_volume(0.05)
        sound.play()
        #Screen
        background = pygame.image.load(self.background_pic)
        background_size = self.screen.get_size()
        background_rect = background.get_rect()
        background_screen = pygame.display.set_mode(background_size)
        background_screen.blit(background, background_rect)
        self.screen.blit(background, background_rect)
        pygame.font.init()
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Choose a Character', False, (255,255,255))
        gator = myfont.render('GATOR', False,(255,153,51))
        bear = myfont.render('BEAR', False, (255,0,0))
        bearcat = myfont.render('BEARCAT', False, (0,153,76))
        gamecock = myfont.render('GAMECOCK', False, (255,153,153))
        pygame.draw.rect(self.screen,(0,0,0),(160,230,100,50)) #gator
        pygame.draw.rect(self.screen,(0,0,0),(324,230,90,50)) #bear
        pygame.draw.rect(self.screen,(0,0,0),(485,230,125,50)) #bearcat
        pygame.draw.rect(self.screen,(0,0,0),(685,230,155,50)) #gamecock
        self.screen.blit(message, [375,150])
        self.screen.blit(gator,[175, 250])
        self.screen.blit(bear,[339, 250])
        self.screen.blit(bearcat,[500, 250])
        self.screen.blit(gamecock,[700, 250])
        pygame.display.flip()
        pygame.key.set_repeat(1000)
        accum = 2
        while accum > 0:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 160 < mouse_pos[0] < 260 and 230 < mouse_pos[1] < 280:
                        if accum == 1:
                            self.p1 = "gator"
                            print(self.p1)
                            accum -= 1
                    if 160 < mouse_pos[0] < 260 and 230 < mouse_pos[1] < 280:
                        if accum == 2:
                            self.p2 = "gator"
                            print(self.p2)
                            accum -= 1
                    if 324 < mouse_pos[0] < 414 and 230 < mouse_pos[1] < 280:
                        if accum == 1:
                            self.p1 = "bear"
                            print(self.p1)
                            accum -= 1
                    if 324 < mouse_pos[0] < 414 and 230 < mouse_pos[1] < 280:
                        if accum == 2:
                            self.p2 = "bear"
                            print(self.p2)
                            accum -= 1
                    if 485 < mouse_pos[0] < 610 and 230 < mouse_pos[1] < 280:
                        if accum == 1:
                            self.p1 = "bearcat"
                            print(self.p1)
                            accum -= 1
                    if 485 < mouse_pos[0] < 610 and 230 < mouse_pos[1] < 280:
                        if accum == 2:
                            self.p2 = "bearcat"
                            print(self.p2)
                            accum -= 1
                    if 685 < mouse_pos[0] < 840 and 230 < mouse_pos[1] < 280:
                        if accum == 1:
                            self.p1 = "gamecock"
                            print(self.p1)
                            accum -= 1
                    if 685 < mouse_pos[0] < 840 and 230 < mouse_pos[1] < 280:
                        if accum == 2:
                            self.p2 = "gamecock"
                            print(self.p2)
                            accum -= 1
        self.state = "GAME"
        self.mainLoop()
    def gameLoop(self):
        # initialize classes to players
        if self.p1 == "bear":
            p1 = bear.Bear()
        elif self.p2 == "bear":
            p2 = bear.Bear()
        if self.p1 == "gator":
            p1 = gator.Gator()
        elif self.p2 == "gator":
            p2 = gator.Gator()
        if self.p1 == "gamecock":
            p1 = gamecock.Gamecock()
        elif self.p2 == "gamecock":
            p2 = gamecock.Gamecock()
        if self.p1 == "bearcat":
            p1 = bearcat.Bearcat()
        elif self.p2 == "bearcat":
            p2 = bearcat.Bearcat()
        #initialize screen
        arena = pygame.image.load(self.arena)
        arena_size = self.screen.get_size()
        arena_rect = arena.get_rect()
        arena_screen = pygame.display.set_mode(arena_size)
        arena_screen.blit(arena, arena_rect)
        self.screen.blit(arena, arena_rect)
        self.screen.blit(p1,[100,500])
        self.screen.blit(p2,[800,500])
        self.display.flip()
        # Initialize new screen with fighters
        # Fight
        # Health bar
        # Sound


        def fight(p1, p2):
            if p1.health > p2.health:
                print(p1.name + " Wins!")
            if p1.health < p2.health:
                print(p2.name + " Wins!")
            if p1.health == p2.health:
                print("wow you both suck")
        fight(p1,p2)
        sys.exit()
