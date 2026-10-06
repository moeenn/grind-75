from unittest import TestCase

from .singleton import Singleton


class TestSingleton(TestCase):
    def test_instantiation(self) -> None:
        one = Singleton()
        two = Singleton()
        self.assertTrue(one is two)
