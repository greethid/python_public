import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Class dedicated to managing the spacecraft"""

    def __init__(self, ai_game):
        """Spacecraft initialization and its initial position"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Loading image of the spacecraft and downloading its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Every new spacecraft appears on the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # The ship's horizontal position is stored as a floating point number
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # Options that indicate the movement of the ship
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Updating the position of the ship based on the option indicating its movement"""
        # Updating the value of the X coordinate of the ship, not its rectangle
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Updating rect based on value self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """Displaying the spacecraft at its current position"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Place the ship in the center at the bottom edge of the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)