import pygame

class Bear(pygame.sprite.Sprite):
    def __init__(self):
    self.health = 200
    self.hit = 150
    self.image = pygame.image.load("assets/images.png")
