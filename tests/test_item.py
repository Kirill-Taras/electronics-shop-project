"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError


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


def test_instantiate_from_csv_filenotfounderror():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('../src/i.csv')


def test_instantiate_from_csv_instantiatecsverror():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('../src/test_items.csv')


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'


def test_add():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Телевизор", 10000, 20)
    assert item1 + item2 == 40
