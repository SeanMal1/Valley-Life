import pygame
from settings import *

#overlay class for player hud and menus
class Overlay:
    #initialisation method
    def __init__(self, player):
        self._DisplaySurface = pygame.display.get_surface()
        self._Player = player
        OverlayPath = '../textures/ui/'

        self._font = pygame.font.Font('../font/joystixmonospace.otf', 18)

        self._ToolsOverlay = {tool: pygame.image.load(f'{OverlayPath}{tool}.png').convert_alpha() for tool in player._Tools}
        self._SeedsOverlay = {seed: pygame.image.load(f'{OverlayPath}{seed}.png').convert_alpha() for seed in player._Seeds}

    #method to display the tool section of the hud
    def display_tools(self):
        pygame.draw.rect(self._DisplaySurface, (255, 255, 255, 0), pygame.Rect(5, ScreenHeight-80, 260, 70), border_radius=4)
        #for loop to iterate through tools to display each
        for (i, tool) in enumerate(self._Player._Tools):
            self._DisplaySurface.blit(pygame.transform.scale(self._ToolsOverlay[tool], (48, 48)), (20 + 60*i, ScreenHeight-70))
            if tool == self._Player._SelectedTool:
                pygame.draw.rect(self._DisplaySurface, (255, 0, 0), pygame.Rect(15 + 60*i, ScreenHeight-75, 58, 58), width=2, border_radius=4)

    #method to display the seed section of the hud
    def display_seed(self):
        pygame.draw.rect(self._DisplaySurface, (255, 255, 255, 0), pygame.Rect(ScreenWidth-80, ScreenHeight-80, 70, 70), border_radius=4)
        self._DisplaySurface.blit(pygame.transform.scale(self._SeedsOverlay[self._Player._SelectedSeed], (48, 48)), (ScreenWidth-75, ScreenHeight-65))

    #method to display the health section of the hud
    def display_health(self):
        #health stat
        self._DisplaySurface.blit(self._font.render("Health: ", False, "Black"), (25, 25))
        pygame.draw.rect(self._DisplaySurface, (0, 255, 0), pygame.Rect(150, 27, self._Player._health * 2, 12))
        #energy stat
        self._DisplaySurface.blit(self._font.render("Energy: ", False, "Black"), (25, 45))
        pygame.draw.rect(self._DisplaySurface, (0, 232, 252), pygame.Rect(150, 47, self._Player._fatigue * 2, 12))
        #hunger stat
        self._DisplaySurface.blit(self._font.render("Hunger: ", False, "Black"), (25, 65))
        pygame.draw.rect(self._DisplaySurface, (252, 44, 0), pygame.Rect(150, 67, self._Player._hunger * 2, 12))

    #method which displays all sections of the hud by calling previous methods
    def Display(self):
        self.display_tools()
        self.display_seed()
        self.display_health()
