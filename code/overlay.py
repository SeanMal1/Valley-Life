import pygame
from settings import *

class Overlay:
    def __init__(self,player):
        self._DisplaySurface = pygame.display.get_surface()
        self._Player = player
        OverlayPath = '../textures/ui/'
        self._ToolsOverlay = {tool:pygame.image.load(f'{OverlayPath}{tool}.png').convert_alpha() for tool in player._Tools}
        self._SeedsOverlay = {}

    def Display(self):
        #seed

        #tool
        ToolOverlay = self._ToolsOverlay[self._Player._SelectedTool]
        ToolScaled = pygame.transform.scale(ToolOverlay,(96,96))
        self._DisplaySurface.blit(ToolScaled,(1184,624))