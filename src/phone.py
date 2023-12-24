from src.item import Item


class Phone(Item):
    """
    Класс для представления телефонов в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, count_simcard: int):
        """
        Создание экземпляра класса phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param count_simcard: Количество Sim-карт.
        """
        super().__init__(name, price, quantity)
        self.count_simcard = count_simcard

    @property
    def number_of_sim(self):
        if not isinstance(self.count_simcard, int) or self.count_simcard <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            return self.count_simcard

    def __add__(self, other):
        if isinstance(other, Phone) or isinstance(other, Item):
            return self.quantily + other.quantily
        else:
            raise ValueError("Объект не пренадлежит классу")

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.name, self.price, self.quantily, self.count_simcard}"
