"""
Game menu view handling.
"""

import pygame


class MenuButton:
    def __init__(self, text: str, dest: tuple) -> None:
        self.text = text
        self.dest = dest
        self.size = (200, 50)

    def draw(self, screen: pygame.Surface):
        font = pygame.font.Font(None, 35)
        text = font.render(self.text, True, "black")
        button = pygame.rect.Rect(self.dest, self.size)
        button_color = "blue" if self.hovering() else "white"
        pygame.draw.rect(screen, button_color, button, border_radius=12)

        x, y = self.dest
        width, height = self.size
        x_pos = (x + (width / 2)) - text.get_width() / 2
        y_pos = (y + (height / 2)) - text.get_height() / 2
        screen.blit(text, (x_pos, y_pos))

    def hovering(self) -> bool:
        """
        Returns the state of mouse cursor hovering.

        :returns: The state of the mouse cursor is hovering or not.
        """

        mouse_x, mouse_y = pygame.mouse.get_pos()
        button_x, button_y = self.dest
        width, height = self.size

        return (mouse_x >= button_x) & (mouse_y >= button_y) & (mouse_x <= (button_x + width)) & (mouse_y <= (button_y + height))


class GameMenu:
    """
    Main menu for the game.
    """

    def __init__(self) -> None:
        self.screen = pygame.display.set_mode((1024, 768))
        pygame.display.set_caption("Platformer")
        pygame.init()

    def render(self):
        # Background
        self.screen.fill((0, 0, 0))

        # Title
        font = pygame.font.Font(None, 40)
        title = font.render("Main Menu", True, "white")
        self.screen.blit(title, ((1024 / 2) - (title.get_width() / 2), 100))

        # Buttons
        play_button = MenuButton("Play", ((self.screen.get_width() / 2) - 100, 200))
        quit_button = MenuButton("Quit", ((self.screen.get_width() / 2) - 100, 300))
        play_button.draw(self.screen)
        quit_button.draw(self.screen)
        pygame.display.flip()
