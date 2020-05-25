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
        self.state = "BEGIN"
        self.run = True
        self.white = (255,255,255)
        

    def mainLoop(self):
        while self.run:
            if self.state == "BEGIN":
                self.gameIntroScreen()
            elif self.state == "GAME":
                self.gameLoop()
            elif self.state == "LOSE":
                self.gameOverScreen()
    def gameIntroScreen(self):
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
        accum = 2
        while accum > 0:
            for event in pygame.event.get():
                if event.key == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if 160 < mouse_pos[0] < 260 and 230 < mouse_pos[1] < 280:
                        if accum == 2:
                            p1 = gator.Gator()
                            accum -= 1
                        if accum == 1:
                            p2 = gator.Gator()
                            accum -= 1
                    if 324 < mouse_pos[0] < 414 and 230 < mouse_pos[1] < 280:
                        if accum == 2:
                            p1 = bear.Bear()
                            accum -= 1
                        if accum == 1:
                            p2 = bear.Bear()
                            accum -= 1
                    if 160 < mouse_pos[0] < 260 and 230 < mouse_pos[1] < 280:
                        if accum == 2:
                            p1 = bearcat.Bearcat()
                            accum -= 1
                        if accum == 1:
                            p2 = bearcat.Bearcat()
                            accum -= 1
                    if 160 < mouse_pos[0] < 260 and 230 < mouse_pos[1] < 280:
                        if accum == 2:
                            p1 = gamecock.Gamecock()
                            accum -= 1
                        if accum == 1:
                            p2 = gamecock.Gamecock()
                            accum -= 1

                self.mainLoop()
