import pygame

class Bearcat(pygame.sprite.Sprite):
    def __init__(self):
    self.health = 100
    self.hit = 15
    self.image = pygame.image.load("assets/binghamton.png")
    
