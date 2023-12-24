from src.item import Item


class Mixin:

    lang_change_count = 1

    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        Mixin.lang_change_count += 1
        if not Mixin.lang_change_count % 2 == 0:
            self.__language = "EN"
        else:
            self.__language = "RU"
        return self.__language


class Keyboard(Item, Mixin):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)





