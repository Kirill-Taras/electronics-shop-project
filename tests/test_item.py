"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item_class():
    test_item = Item("Смартфон", 10, 5)

    assert test_item.calculate_total_price() == 50

    Item.pay_rate = 1.5
    test_item.apply_discount()
    assert test_item.price == 15


def test_string_to_number():
    assert Item.string_to_number('77') == 77


def test_instantiate_from_csv():
    Item.instantiate_from_csv('../src/items.csv')
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
