"""
Tests for the events module.
"""

import gc

from platformer.events import EventListener, EventManager


class MockListener(EventListener):
    def update(self):
        return super().update()


class TestEventManager:
    """
    Tests for the Event Manager class.
    """

    def test_instantiate(self):
        """
        Test the instantiation of the Event Manager class as the initial state of listeners.
        """

        event_manager = EventManager()

        assert event_manager is not None
        assert len(event_manager.listeners) == 0

    def test_register_event(self):
        """
        Test the register event method.
        """

        event_listener = MockListener()
        event_manager = EventManager()

        event_manager.register(event_listener)

        assert len(event_manager.listeners) == 1

    def test_unregister_event(self):
        """
        Test the unregister event method.
        """

        event_listener = MockListener()
        event_manager = EventManager()

        event_manager.register(event_listener)

        assert len(event_manager.listeners) == 1

        event_manager.unregister(event_listener)

        assert len(event_manager.listeners) == 0

    def test_weakref(self):
        """
        Test the weak reference behavior.
        """

        event_listener = MockListener()
        event_manager = EventManager()

        event_manager.register(event_listener)

        assert len(event_manager.listeners) == 1

        del event_listener
        gc.collect()

        assert len(event_manager.listeners) == 0
