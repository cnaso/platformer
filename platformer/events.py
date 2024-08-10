"""
Contains event management for the game.
"""

from enum import Enum, auto
from typing import Any
from weakref import WeakKeyDictionary


class GameEvent:
    """
    Game event base class.
    """

    def __str__(self) -> str:
        keywords = [f"{key}={value!r}" for key, value in self.__dict__.items()]

        return "{}({})".format(type(self).__name__, ", ".join(keywords))


class QuitEvent(GameEvent):
    """
    Quit event.
    """

    def __init__(self) -> None:
        super().__init__()


class InputEvent(GameEvent):
    """
    Input event.
    """

    def __init__(self, key: int, mouse_button: int, click_position: tuple) -> None:
        super().__init__()
        self.key = key
        self.mouse_button = mouse_button
        self.click_position = click_position


class EventManager:
    """
    Manages communication between listeners.
    """

    def __init__(self) -> None:
        self.listeners = WeakKeyDictionary()

    def register(self, listener: Any) -> None:
        """
        Registers a listener for events.

        :param listener: The listener to be registered.
        """

        self.listeners[listener] = 1

    def unregister(self, listener: Any) -> None:
        """
        Un-registers a listener for events. weakref implementation auto removes non-existing listeners.

        :param listener: The listener to be un-registered.
        """

        self.listeners.pop(listener)

    def notify(self, event: GameEvent) -> None:
        """
        Notifies listeners of event.

        :param event: The event to notify listeners for.
        """

        for listener in self.listeners:
            listener.update(event)
