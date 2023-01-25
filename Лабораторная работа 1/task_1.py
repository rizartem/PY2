# TODO Написать 3 класса с документацией и аннотацией типов

class Tree:
    def __init__(self, leaf: int, orange_leaf: int, age: int):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param leaf: Количество листьев на дереве
        :param orange_leaf: Количество пожелтевших листьев
        :param age: Возраст дерева

        Пример:
        >>> tree = Tree(1000, 650, 3)
        """
        if not isinstance(leaf, int):
            raise TypeError("Число листьев на дереве должно быть типа int")
        if leaf <= 0:
            raise ValueError("Число листьев на дереве должно быть положительным числом")
        self.leaf = leaf

        if not isinstance(orange_leaf, int):
            raise TypeError("Число пожелтевших листьев на дереве должно быть типа int")
        if orange_leaf < 0 or orange_leaf > leaf:
            raise ValueError("Число пожелтевших листьев на дереве должно быть положительным числом, не превышающим число всех листьев")
        self.orange_leaf = orange_leaf

        if not isinstance(age, int):
            raise TypeError("Возраст дерева должен быть типа int")
        if age <= 0:
            raise ValueError("Возраст дерева должен быть положительным числом")
        self.age = age

    def increase_orange_leaf(self, yellowed_leaves: int):
        """
        етод увеличивает число пожелтевших листев на дереве,
        проверяя тип yellowed_leaves и итоговое число пожелтевших листьев (чтобы не превышало число всех листьев)

        :param yellowed_leaves: Количество пожелтевших листьев
        :return: Новое число пожелтевших листьев

        Пример:
        >>> tree = Tree(1000, 650, 3)
        >>> tree.increase_orange_leaf(200)
        """
        ...

    def increase_age(self, time_: int):
        """
        Метод увеличивает возраст дерева

        :param time_: прошедшее время
        :return: Новый возраст дерева

        Пример:
        >>> tree = Tree(1000, 650, 3)
        >>> tree.increase_age(10)
        """
        ...


class Forest:
    def __init__(self, trees: int, birchs: int, oak: int):
        """
        Создание и подготовка к работе объекта "Лес"

        :param trees: Количество деревьев в лесу
        :param birchs: Количество берез в лесу
        :param oak: Количество дубов в лесу

        Пример:
        >>> forest = Forest(500, 100, 100)
        """
        if not isinstance(trees, int):
            raise TypeError("Количество деревьев в лесу должно быть типа int")
        if trees <= 0:
            raise ValueError("Количество деревьев в лесу должно быть положительным числом")
        self.trees = trees

        if not isinstance(birchs, int):
            raise TypeError("Количество берез в лесу должно быть типа int")
        if birchs < 0:
            raise ValueError("Количество берез в лесу должно быть положительным числом")
        if birchs > trees:
            raise ValueError("Количество берез в лесу не должно превышать количество всех деревьев")
        self.birchs = birchs

        if not isinstance(oak, int):
            raise TypeError("Количество дубов в лесу должно быть типа int")
        if oak < 0:
            raise ValueError("Количество дубов в лесу должно быть положительным числом")
        if oak + birchs > trees:
            raise ValueError("Количество дубов и берез в лесу не должно превышать количество всех деревьев")
        self.aspens = oak

    def new_brichs(self, brich_seeds: int):
        """
        Метод увеличивает количество берез в лесу и прибавляет к общей численности

        :param brich_seeds: Количество новых посаженных берез
        :return: Общее число берез

        Пример:
        >>> forest = Forest(500, 100, 100)
        >>> forest.new_brichs(50)
        """
        ...

    def new_oak(self, oak_seeds: int):
        """
        Метод увеличивает количество дубов в лесу и прибавляет к общей численности

        :param oak_seeds:
        :return: Общее число дубов

        Пример:
        >>> forest = Forest(500, 100, 100)
        >>> forest.new_oak(50)
        """
        ...


class Table:
    def __init__(self, material: str, table_leg: int):
        """
        Создание и подготовка к работе объекта "Стол"

        :param material: Материал столешницы
        :param table_leg: Количество ножек стола

        Пример:
        >>> table = Table('дерево', 4)
        """
        if not isinstance(material, str):
            raise TypeError("Материал стола должен быть типа str")
        self.material = material

        if not isinstance(table_leg, int):
            raise TypeError("Количество ножек у стола должно быть типа int")
        if table_leg <= 0:
            raise ValueError("Количество ножек у стола должно быть положительным числом")
        self.table_leg = table_leg
        self.item = None

    def add_item_(self, item: str):
        """
        Метод добавляет предмет на стол

        :param item: предмет
        :return: добавляет в атрибут предмет

        Пример:
        >>> table = Table('дерево', 4)
        >>> table.add_item_('яблоко')
        """
        ...

    def broke_leg(self, crush_leg):
        """
        Метод вычитает из количества ножек стола сломанные

        :param crush_leg: Количество сломанных ножек
        :return: Количество оставшихся целых ножек

        Пример:
        >>> table = Table('дерево', 4)
        >>> table.broke_leg(1)
        """
        ...


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
