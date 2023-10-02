import unittest
from parameterized import parameterized
from gilded_rose import BaseItem, BackstagePasses


class GildedRoseTest(unittest.TestCase):
    def test_general_positive_sell_in(self):
        g_item = BaseItem("general", 1, 10)
        g_item.update_item()

        expected_sell_in = 0
        expected_quality = 9

        self.assertEqual(g_item.sell_in, expected_sell_in)
        self.assertEqual(g_item.quality, expected_quality)

    def test_general_zero_sell_in(self):
        g_item = BaseItem("general", 0, 10)
        g_item.update_item()

        expected_sell_in = -1
        expected_quality = 8

        self.assertEqual(g_item.sell_in, expected_sell_in)
        self.assertEqual(g_item.quality, expected_quality)

    def test_general_negative_sell_in(self):
        g_item = BaseItem("general", -1, 10)
        g_item.update_item()

        expected_sell_in = -2
        expected_quality = 8

        self.assertEqual(g_item.sell_in, expected_sell_in)
        self.assertEqual(g_item.quality, expected_quality)

    @parameterized.expand([
        [10, 9, 3, 4],
        [1, 0, 1, 2]
    ])
    def test_aged_brie_quality_rise_sell_above_zero(self, sell_in_init, sell_in_expected, quality_init, quality_expected):
        g_item = BaseItem("Aged Brie", sell_in_init, quality_init, quality_change=1)
        g_item.update_item()
        self.assertEqual(sell_in_expected, g_item.sell_in)
        self.assertEqual(quality_expected, g_item.quality)

    @parameterized.expand([
        [0, -1, 1, 3],
        [-1, -2, 1, 3]
    ])
    def test_aged_brie_quality_rise_sell_belove_zero(self, sell_in_init, sell_in_expected, quality_init, quality_expected):
        g_item = BaseItem("Aged Brie", sell_in_init, quality_init, quality_change=1)
        g_item.update_item()
        self.assertEqual(sell_in_expected, g_item.sell_in)
        self.assertEqual(quality_expected, g_item.quality)
    
    @parameterized.expand([        
        [-1, -2, 48, 50],
        [-1, -2, 49, 50],
        [-1, -2, 50, 50]
    ])
    def test_aged_brie_quality_rise_above_max_value(self, sell_in_init, sell_in_expected, quality_init, quality_expected):
        g_item = BaseItem("Aged Brie", sell_in_init, quality_init, quality_change=1)
        g_item.update_item()
        self.assertEqual(sell_in_expected, g_item.sell_in)
        self.assertEqual(quality_expected, g_item.quality)


    @parameterized.expand([        
        [20, 19, 1, 2],
        [20, 19, 11, 12],
    ])
    def test_backstage_passes_quality_rise_normal(self, sell_in_init, sell_in_expected, quality_init, quality_expected):
        g_item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", sell_in_init, quality_init, quality_change=1)
        g_item.update_item()
        self.assertEqual(sell_in_expected, g_item.sell_in)
        self.assertEqual(quality_expected, g_item.quality)

    @parameterized.expand([        
        [11, 10, 1, 2],
        [10, 9, 1, 3],
        [9, 8, 1, 3],
    ])
    def test_backstage_passes_quality_rise_near_10_sell(self, sell_in_init, sell_in_expected, quality_init, quality_expected):
        g_item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", sell_in_init, quality_init, quality_change=1)
        g_item.update_item()
        self.assertEqual(sell_in_expected, g_item.sell_in)
        self.assertEqual(quality_expected, g_item.quality)

    @parameterized.expand([        
        [6, 5, 1, 3],
        [5, 4, 1, 4],
        [4, 3, 1, 4],
    ])
    def test_backstage_passes_quality_rise_near_5_sell(self, sell_in_init, sell_in_expected, quality_init, quality_expected):
        g_item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", sell_in_init, quality_init, quality_change=1)
        g_item.update_item()
        self.assertEqual(sell_in_expected, g_item.sell_in)
        self.assertEqual(quality_expected, g_item.quality)

    @parameterized.expand([        
        [1, 0, 3, 6],
        [0, -1, 100, 0],
        [0, -1, 40, 0],
    ])
    def test_backstage_passes_quality_rise_near_0_sell(self, sell_in_init, sell_in_expected, quality_init, quality_expected):
        g_item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", sell_in_init, quality_init, quality_change=1)
        g_item.update_item()
        self.assertEqual(sell_in_expected, g_item.sell_in)
        self.assertEqual(quality_expected, g_item.quality)

    @parameterized.expand([        
        [10, 9, 80, 50],
        [10, 9, 100, 50],
        [10, 9, 49, 50],
        [5, 4, 48, 50],
        [2, 1, 48, 50],
    ])
    def test_backstage_passes_quality_rise_above_max_value(self, sell_in_init, sell_in_expected, quality_init, quality_expected):
        g_item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", sell_in_init, quality_init, quality_change=1)
        g_item.update_item()
        self.assertEqual(sell_in_expected, g_item.sell_in)
        self.assertEqual(quality_expected, g_item.quality)

    @parameterized.expand([        
        [-1, -2, 3, 0],
        [-1, -2, 100, 0],
        [-1, -2, 40, 0],
    ])
    def test_backstage_passes_quality_drop_after_concert(self, sell_in_init, sell_in_expected, quality_init, quality_expected):
        g_item = BackstagePasses("Backstage passes to a TAFKAL80ETC concert", sell_in_init, quality_init, quality_change=1)
        g_item.update_item()
        self.assertEqual(sell_in_expected, g_item.sell_in)
        self.assertEqual(quality_expected, g_item.quality)


if __name__ == '__main__':
    unittest.main()
