"""
Contains game state and input handling.
"""

import sys

import pygame

from platformer.events import EventListener, EventManager, GameEvent, QuitEvent
from platformer.menu import GameMenu


class GameController(EventListener):
    """
    Handles game state and input from the user, delegates events and behavior.
    """

    def __init__(self, event_manager: EventManager) -> None:
        """
        :param event_manager: The event manager class instance.
        """

        self.event_manager = event_manager
        self.event_manager.register(self)
        self.running = True

    def update(self):
        for pygame_event in pygame.event.get():
            if pygame_event.type == pygame.QUIT:
                self.event_manager.notify(QuitEvent())
                break

            keys = pygame.key.get_pressed()

            # if keys[pygame.K_LEFT]:
            #     self.player.x_movement = -4

            # if keys[pygame.K_RIGHT]:
            #     if self.player.rect.x < 512:
            #         self.player.x_movement = 4
            #     elif self.player.rect.x >= 512:
            #         self.player.x_movement = 0
            #         self.camera_x += 4

            # if keys[pygame.K_SPACE]:
            #     self.player.jump()

            # TODO: Check if this is even necessary and if so why
            # if not keys[pygame.K_LEFT] | keys[pygame.K_RIGHT]:
            #     self.player.x_movement = 4
            #     self.player.x_movement = 0

    def run(self):
        clock = pygame.time.Clock()
        menu = GameMenu()

        while self.running:
            self.update()
            menu.render()
            clock.tick(60)

        pygame.quit()
        sys.exit()
