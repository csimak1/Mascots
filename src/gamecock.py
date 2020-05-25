import pygame
import random

class Gamecock(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "South Carolina"
        self.person = "Joe"
        self.health = random.randint(5,15)
        self.image = pygame.image.load("assets/gamecock.png")
