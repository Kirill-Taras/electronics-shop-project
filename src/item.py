import csv


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantily = quantity
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantily

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self) -> str:
        """
        Геттер для name.
        """
        return self.__name

    @name.setter
    def name(self, name) -> None:
        """
        Обрезает строку до 10 символов.
        """
        self.__name = name[0:10]

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """
        Класс-метод, инициализирующий экземпляры класса Item данными из файла .csv.
        """
        cls.all = []
        with open(file_name, newline='', encoding='windows-1251') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                name, price, quantity = row['name'], float(row['price']), int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(number) -> int:
        """
        Статический метод, возвращающий число из числа-строки.
        """
        if isinstance(number, str):
            int_number = float(number)
            return int(int_number)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.__name, self.price, self.quantily}"

    def __str__(self) -> str:
        return self.__name
