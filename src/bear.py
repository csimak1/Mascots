import pygame
import random

class Bear(pygame.sprite.Sprite):
    def __init__(self):
        self.name = "Cornell"
        self.person = "Pat"
        self.health = random.randint(100,200)
        self.image = pygame.image.load("assets/images.png")

 def fight(p1, p2):
    if p1.health > p2.health:
        print(p1.name + " Wins!")
    if p1.health < p2.health:
        print(p2.name + " Wins!")
    if p1.health == p2.health:
        print("wow you both suck")
