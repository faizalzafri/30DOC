from abc import ABCMeta, abstractmethod


class Book(object, metaclass=ABCMeta):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(): pass


# Write MyBook class
class MyBook(Book):
    def __init__(self, book_title, book_author, book_price):
        super(MyBook, self).__init__(book_title, book_author)
        self.book_price = book_price

    def display(self):
        print('Title: {}\nAuthor: {}\nPrice: {}'.format(title, author, self.book_price))


title = input()
author = input()
price = int(input())
new_novel = MyBook(title, author, price)
new_novel.display()
