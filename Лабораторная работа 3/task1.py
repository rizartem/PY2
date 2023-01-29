class Book:
    """ Базовый класс книги. """

    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def author(self):
        return self._author

    @property
    def name(self):
        return self._name



class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}, Страниц в книге {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if new_pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self._pages = new_pages


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        # self.name = name
        # self.author = author
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Продолжительность {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        if not isinstance(new_duration, float):
            raise TypeError("Продолжительность аудиокниги должна быть типа float")
        if new_duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть положительным числом")
        self._duration = new_duration


book_1 = Book("Ведьмак", "Сапковский")
print(book_1)
book_2 = PaperBook("Ведьмак", "Сапковский", 500)
print(book_2)
book_3 = AudioBook("Ведьмак", "Сапковский", 500.0)
print(book_3)

