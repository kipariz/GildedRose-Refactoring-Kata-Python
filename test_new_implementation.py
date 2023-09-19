import unittest
from gilded_rose import ItemBase


class GildedRoseTest(unittest.TestCase):
    def test_general_positive_sell_in(self):
        g_item = ItemBase("general", 1, 10)
        g_item.update_item()

        expected_sell_in = 0
        expected_quality = 9

        self.assertEqual(g_item.sell_in, expected_sell_in)
        self.assertEqual(g_item.quality, expected_quality)

    def test_general_zero_sell_in(self):
        g_item = ItemBase("general", 0, 10)
        g_item.update_item()

        expected_sell_in = -1
        expected_quality = 8

        self.assertEqual(g_item.sell_in, expected_sell_in)
        self.assertEqual(g_item.quality, expected_quality)

    def test_general_negative_sell_in(self):
        g_item = ItemBase("general", -1, 10)
        g_item.update_item()

        expected_sell_in = -2
        expected_quality = 8

        self.assertEqual(g_item.sell_in, expected_sell_in)
        self.assertEqual(g_item.quality, expected_quality)
