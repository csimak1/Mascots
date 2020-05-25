import pygame
import random

class Gator(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.name = "Florida"
        self.person = "Bryan"
        self.health = random.randint(10,50)
        self.image = pygame.image.load("assets/gators.png")
