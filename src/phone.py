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
        self.__count_simcard = count_simcard

    @property
    def number_of_sim(self):
        return self.__count_simcard

    @number_of_sim.setter
    def number_of_sim(self, count_simcard):
        if not isinstance(count_simcard, int) or count_simcard <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self.__count_simcard = count_simcard

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.name, self.price, self.quantily, self.__count_simcard}"
