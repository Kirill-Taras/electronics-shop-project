from src.item import Item


class Mixin:

    lang_change_count = 1

    def __init__(self):
        self.language = "EN"

    def change_lang(self):
        Mixin.lang_change_count += 1
        if not Mixin.lang_change_count % 2 == 0:
            self.language = "EN"
        else:
            self.language = "RU"
        return self.language


class Keyboard(Item, Mixin):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.language = "EN"




