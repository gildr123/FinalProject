import pygame
from pygame import Surface
from pygame.event import Event
from asset import Asset


class CheckeredBackground(Asset):
    """
    Asset for the background image in the menus for checkers.

    Parameters:
        image_path (str): The path to the background image file.

    Attributes:
        image: The background image.
    """

    def __init__(self, image_path):
        super().__init__(pygame.Vector2(0, 0))
        self.image = pygame.image.load(image_path)

    def process(self, events: list[Event]) -> None:
        """Process events for the background (no movement)."""
        pass

    def draw(self, screen: Surface) -> None:
        """Draws the background image on the screen, scaling it to cover the whole screen."""
        screen_width, screen_height = screen.get_size()
        scaled_image = pygame.transform.scale(self.image, (screen_width, screen_height))
        screen.blit(scaled_image, self.position)