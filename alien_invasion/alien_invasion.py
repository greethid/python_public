import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """General class dedicated to managing the resources and the way the game works."""

    def __init__(self):
        """Initialize game and create resources."""

        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Start main loop of the program"""

        while True:
            #Waiting for input from a user
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            #Refresh screen after each iteration of the loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            #Displaying the last modified screen
            pygame.display.flip()


if __name__ == '__main__':
    #Creating a copy of the game and launching it
    ai = AlienInvasion()
    ai.run_game()

