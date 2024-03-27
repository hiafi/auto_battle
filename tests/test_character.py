import random
import unittest

from auto_battler.actors import PlayerCharacter

class TestCharacter(unittest.TestCase):
    def setUp(self):
        random.seed(0)
        self.character = PlayerCharacter("Test", 10, 0)

    def test_take_damage(self):
        self.assertEqual(self.character.take_damage(5), 5)
        self.assertEqual(self.character.hp, 5)

    def test_get_damage(self):
        self.assertEqual(self.character.get_damage(), 4)
