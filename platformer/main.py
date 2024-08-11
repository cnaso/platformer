"""
Main entry point for the game. Creates the Game object and starts the game loop.
"""

from platformer.controller import GameController
from platformer.events import EventManager

# from platformer.game import Game


def main():
    event_manager = EventManager()

    game_controller = GameController(event_manager)
    game_controller.run()


if __name__ == "__main__":
    main()
