# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            new_quality = item.quality
            new_sell_in = item.sell_in

            if item.name == "Aged Brie" or item.name == "Backstage passes to a TAFKAL80ETC concert":
                if new_quality < 50:
                    new_quality = new_quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
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


class BaseItem(Item):
    def __init__(self, name, sell_in, quality, quality_change=-1, quality_degradation_factor=2):
        Item.__init__(self, name, sell_in, quality)
        self.quality_change = quality_change
        self.quality_degradation_factor = quality_degradation_factor

    def update_quality(self):
        if self.sell_in > 0:
            self.quality += self.quality_change
        else:
            self.quality += self.quality_change * self.quality_degradation_factor
        
        if self.quality > 50:
            self.quality = 50

    def update_sell_in(self):
        self.sell_in -= 1

    def update_item(self):
        self.update_quality()
        self.update_sell_in()

