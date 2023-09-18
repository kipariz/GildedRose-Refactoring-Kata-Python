# -*- coding: utf-8 -*-
import unittest
from parameterized import parameterized

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_general_item(self):
        items = [Item("foo", 2, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)
        self.assertEquals(1, items[0].quality)

    def test_general_item_expired(self):
        items = [Item("foo", 0, 2)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)
        self.assertEquals(0, items[0].quality)

    def test_update_quality_sets_zero_quality_when_expired_item_zero_quality_passed(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(0, items[0].quality)
        
    @parameterized.expand([
        [1, 0, 1, 2],
        [0, -1, 1, 3],
        [-1, -2, 1, 3],
    ])
    def test_aged_brie_quality_rise(self, sell_in_init, sell_in_expected, quality_init, quality_expected):
        items = [Item("Aged Brie", sell_in_init, quality_init)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(sell_in_expected, items[0].sell_in)
        self.assertEquals(quality_expected, items[0].quality)

    def test_general_item_quality_under_fifty(self):
        items = [Item("Aged Brie", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    @parameterized.expand([
        [-2, 80],
        [3, 50],
        [0, 0],
        [0, -10],
    ])
    def test_legendary_item(self, sell_in_init, quality_init):
        items = [Item("Sulfuras, Hand of Ragnaros", sell_in_init, quality_init)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(sell_in_init, items[0].sell_in)
        self.assertEquals(quality_init, items[0].quality)
    
  
    @parameterized.expand([
        [20, 19, 1, 2],
        [11, 10, 1, 2],
        [10, 9, 1, 3],
        [9, 8, 1, 3],
        [6, 5, 1, 3],
        [5, 4, 1, 4],
        [4, 3, 1, 4],
        [0, -1, 3, 0],
        [-1, -2, 100, 0],
    ])
    def test_backstage_passes(self, sell_in_init, sell_in_expected, quality_init, quality_expected):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in_init, quality_init)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(sell_in_expected, items[0].sell_in)
        self.assertEquals(quality_expected, items[0].quality)

    # "Conjured" items degrade in Quality twice as fast as normal items
    # Not yet implemented
    def test_conjured_item_quality_under_fifty(self):
        items = [Item("Conjured", 1, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    @parameterized.expand([
        [2, 1, 3, 1],
        [1, 0, 1, 0],
        [0, -1, 1, 0],
        [0, -1, 5, 1],
        [-1, -2, 5, 1],
    ])
    def test_conjured_qaulity_decrease(self, sell_in_init, sell_in_expected, quality_init, quality_expected):
        items = [Item("Conjured", sell_in_init, quality_init)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(sell_in_expected, items[0].sell_in)
        self.assertEquals(quality_expected, items[0].quality)


if __name__ == '__main__':
    unittest.main()
