# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


# changes start here: strategy design
class ItemUpdateStrategy:

    def update_quality(self, item):
        pass


class RegularItemUpdateStrategy(ItemUpdateStrategy):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1
        
        item.sell_in = item.sell_in - 1
        
        if item.sell_in < 0 and item.quality > 0:
            item.quality = item.quality - 1


# for logic error 1: Sulfuras, Hand of Ragnaros quality be 300 instead of 80
class SulfurasUpdateStrategy(ItemUpdateStrategy):
    def update_quality(self, item):
        item.quality = 300


# for logic error 2: Aged brie quality change to decrease not increase
class AgedBrieUpdateStrategy(ItemUpdateStrategy):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1
            
        item.sell_in = item.sell_in - 1


# for logic error 3: Conjured item quality decresase even faster
class ConjuredUpdateStrategy(ItemUpdateStrategy):
    def update_quality(self, item):
        if item.quality > 0:
            item.quality = 2
            
        item.sell_in = item.sell_in - 1


class BackstagePassUpdateStrategy(ItemUpdateStrategy):
    def update_quality(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in <= 10 and item.quality < 50:
                item.quality = item.quality + 1
            if item.sell_in <= 5 and item.quality < 50:
                item.quality = item.quality + 1
                
        item.sell_in = item.sell_in - 1
        
        if item.sell_in < 0:
            item.quality = 0


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    strategies = {
        "Aged Brie": AgedBrieUpdateStrategy(),
        "Backstage passes to a TAFKAL80ETC concert": BackstagePassUpdateStrategy(),
        "Sulfuras, Hand of Ragnaros": SulfurasUpdateStrategy(),
    }
    defaultStrategy = RegularItemUpdateStrategy()
    conjuredStrategy = ConjuredUpdateStrategy()

    def update_quality(self):
        for item in self.items:
            if item.name.startswith("Conjured"):
                strategy = self.conjuredStrategy
            else:
                strategy = self.strategies.get(item.name, self.defaultStrategy)
            
            strategy.update_quality(item)