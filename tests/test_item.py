"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

test_item = Item("Смартфон", 10, 5)

assert test_item.calculate_total_price() == 50

Item.pay_rate = 1.5
test_item.apply_discount()
assert test_item.price == 15
