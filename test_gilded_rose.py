# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # example of test that checks for logical errors
    def test_sulfuras_should_not_decrease_quality(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        sulfuras_item = items[0]
        self.assertEqual(80, sulfuras_item.quality)
        self.assertEqual(4, sulfuras_item.sell_in)
        self.assertEqual("Sulfuras", sulfuras_item.name)

    # example of test that checks for syntax errors
    def test_gilded_rose_list_all_items(self):
        items = [Item("Sulfuras", 5, 80)]
        gilded_rose = GildedRose(items)
        all_items = gilded_rose.get_item()
        self.assertEqual(["Sulfuras"], all_items)

    # logic error 1: Sulfuras, Hand of Ragnaros quality be 300 instead of 80
    def test_sulfuras_quality_should_remain_80(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 36, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(300, items[0].quality)
    
    # logic error 2: Aged brie quality change to decrease not increase
    def test_brie_quality_should_remain_increase(self):
        items = [Item("Aged Brie", 36, 20)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(19, items[0].quality)
    
    # logic error 3: Conjured item quality decresase even faster
    def test_conjured_items_should_degrade_by_2(self):
        items = [Item("Conjured Pizza", 36, 16)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2, items[0].quality)

    # syntax errors 1: call get quality
    def test_call_get_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 36, 80)]
        gilded_rose = GildedRose(items)
        with self.assertRaises(AttributeError):
            gilded_rose.get_quality()  

if __name__ == '__main__':
    unittest.main()


