# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            new_quality = item.quality
            new_sell_in = item.sell_in

            if item.name == "Aged Brie":
                if new_quality < 50:
                    new_quality = new_quality + 1
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                if new_quality < 50:
                    new_quality = new_quality + 1
                    if new_quality < 50:
                        if new_sell_in < 11:
                            new_quality = new_quality + 1
                        if new_sell_in < 6:
                            new_quality = new_quality + 1
            else:
                if new_quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        new_quality = new_quality - 1

            if item.name == "Sulfuras, Hand of Ragnaros":
                item.quality = new_quality
                item.sell_in = new_sell_in
                continue
            else:
                new_sell_in = new_sell_in - 1

            if new_sell_in < 0:
                if item.name == "Aged Brie":
                    if new_quality < 50:
                        new_quality = new_quality + 1
                else:
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        new_quality = 0
                    else:
                        if new_quality > 0:
                            new_quality = new_quality - 1
        
        item.quality = new_quality
        item.sell_in = new_sell_in


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
