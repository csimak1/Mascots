import pygame
import random

class Bear(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Cornell"
        self.person = "Pat"
        self.health = random.randint(100,200)
        self.image = pygame.image.load("assets/bear.png")
