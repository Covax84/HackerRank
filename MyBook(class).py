from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self):
        pass


class MyBook(Book):
    def __init__(self, title: str, author: str, price: int):
        super().__init__(title, author)
        self.price = price

    def display(self) -> print:
        print('Title: ' + self.title)
        print('Author: ' + self.author)
        print('Price: ' + str(self.price))


title = input('Enter title: ')
author = input('Enter author: ')
price = int(input('Enter price: '))
my_novel = MyBook(title, author, price)
my_novel.display()
