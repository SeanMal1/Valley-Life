import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((30,56))
        self.image.fill('white')
        self.rect = self.image.get_rect(center = pos)

        #moving attribute
        self._Direction = pygame.math.Vector2()
        self._Position = pygame.math.Vector2(self.rect.center)
        self._Speed = 110

    def input(self):
        keystroke = pygame.key.get_pressed()
        if keystroke[pygame.K_w]:
            self._Direction.y = -1
        elif keystroke[pygame.K_s]:
            self._Direction.y = 1
        else:
            self._Direction.y = 0

        if keystroke[pygame.K_a]:
            self._Direction.x = -1
        elif keystroke[pygame.K_d]:
            self._Direction.x = 1
        else:
            self._Direction.x = 0
        
    def move(self,DeltaTime):
        self._Position += self._Direction * self._Speed * DeltaTime
        self.rect.center = self._Position
        
    def update(self,DeltaTime):
        self.input()
        self.move(DeltaTime)