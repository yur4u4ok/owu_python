from abc import ABC, abstractmethod


# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
#   + сумма площин двох екземплярів ксласу
#   - різниця площин двох екземплярів ксласу
#   == площин на рівність
#   != площин на не рівність
#   >, < меньше більше
#   при виклику метода len() підраховувати сумму сторін
#
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return self.x * self.y + other.x * other.y

    def __sub__(self, other):
        return self.x * self.y - other.x * other.y

    def __eq__(self, other):
        return self.x * self.y == other.x * other.y

    def __lt__(self, other):
        return self.x * self.y < other.x * other.y

    def __gt__(self, other):
        return self.x * self.y > other.x * other.y

    def __len__(self):
        return self.x + self.y


rect = Rectangle(5, 7)
rect1 = Rectangle(4, 5)

print(rect + rect1)
print(rect - rect1)
print(rect == rect1)
print(rect < rect1)
print(rect > rect1)
print(len(rect1))


# ###############################################################################
#
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок,
# та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
#
print('-' * 40)
class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


class Prince(Human):
    def __init__(self, name: str, age: int, searched_shoe_size: int):
        super().__init__(name, age)
        self.searched_shoe_size = searched_shoe_size

    def look_for_size(self, *args):
        for cinderella in args:
            if cinderella.foot_size == self.searched_shoe_size:
                return f"{cinderella.name} {cinderella.age} {cinderella.foot_size}"


class Cinderella(Human):
    count = 0

    def __init__(self, name: str, age: int, foot_size: int):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


cin = Cinderella("Popelyushka", 18, 37)
cin2 = Cinderella("Popelyushka2", 20, 34)
cin3 = Cinderella("Popelyushka3", 19, 38)
prince = Prince("Prince", 22, 34)
print(prince.look_for_size(cin, cin2, cin3))


#
# ###############################################################################
#
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()


class Printable(ABC):
    @abstractmethod
    def print(self):
        pass


# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable

class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Book - '{self.name}'")


class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Magazine - '{self.name}'")


# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають
# є класом Book або Magazine инакше ігрнорувати додавання
# - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
# - метод show_all_books який буде виводити всі книги викликаючи метод print абстрактного классу

class Main:
    printable_list = []

    @classmethod
    def add(cls, class_instance):
        if isinstance(class_instance, Book) or isinstance(class_instance, Magazine):
            cls.printable_list.append(class_instance)

    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


# Приклад:
#
print('-' * 40)

Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))
#
Main.show_all_magazines()

print('-' * 40)

Main.show_all_books()