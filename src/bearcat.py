import pygame
import random

class Bearcat(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Binghamton"
        self.person = "Zac"
        self.health = random.randint(1,300)
        self.image = pygame.image.load("assets/binghamton.png")
