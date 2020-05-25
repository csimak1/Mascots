import pygame

class Gator(pygame.sprite.Sprite):
    def __init__(self):
        self.health = 100
        self.hit = 10
        self.image = pygame.image.load("assets/gators.png")
