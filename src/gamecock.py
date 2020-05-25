import pygame

class Gamecock(pygame.sprite.Sprite):
    def __init__(self):
    self.health = 100
    self.hit = 1
    self.image = pygame.image.load("assets/gamecock.png")
