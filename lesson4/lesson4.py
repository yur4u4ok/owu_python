# 1) Є ось такий файл... ваша задача записати в новий файл тільки email'ли
# з доменом gmail.com (Хеш то що з ліва записувати не потрібно)

with open('emails.txt') as file:
    for line in file:
        if line.endswith('@gmail.com\n'):
            with open("newEmails.txt", 'a') as newFile:
                newFile.write(line.split('\t')[3])
    print('done')


# 2) Створити записну книжку покупок:
# - у покупки повинна бути id, назва і ціна
# - всі покупки зберігаємо в файлі
#   з функціоналу:
# * вивід всіх покупок
# * має бути змога додавати покупку в книгу
# * має бути змога шукати по будь якому полю покупку
# * має бути змога показати найдорожчу покупку
# * має бути можливість видаляти покупку по id
# (ну і меню на це все)


class Purchase:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def add_purchase(self):
        with open('purchases.txt', 'a') as file:
            file.write(f"{self.id} {self.name} {self.price}\n")

    @staticmethod
    def search_product(item, value):
        with open("purchases.txt") as file:
            match item:
                case 'id':
                    for line in file:
                        product_from_file = line.split(' ')

                        if value == product_from_file[0]:
                            print("*" * 20)
                            print(f'Product ID = {product_from_file[0]}')
                            print(f'Name = {product_from_file[1]}')
                            print(f'Price = {product_from_file[2]}')
                            print("*" * 20)
                case 'name':
                    for line in file:
                        product_from_file = line.split(' ')

                        if value == product_from_file[1]:
                            print("*" * 20)
                            print(f'Product ID = {product_from_file[0]}')
                            print(f'Name = {product_from_file[1]}')
                            print(f'Price = {product_from_file[2]}')
                            print("*" * 20)
                case 'price':
                    for line in file:
                        product_from_file = line.split(' ')

                        if f'{value}\n' == product_from_file[2]:
                            print("*" * 20)
                            print(f'Product ID = {product_from_file[0]}')
                            print(f'Name = {product_from_file[1]}')
                            print(f'Price = {product_from_file[2]}')
                            print("*" * 20)

    @staticmethod
    def most_expensive_product():
        with open("purchases.txt") as file:
            max_price = 0
            product_id = 0
            product_name = 0

            for line in file:
                price_from_split_line = int(line.split(' ')[2])
                name_from_line = line.split(' ')[1]
                id_from_line = line.split(' ')[0]

                if price_from_split_line > max_price:
                    max_price = price_from_split_line
                    product_id = id_from_line
                    product_name = name_from_line

            print("*" * 20)
            print(f'Product ID = {product_id}')
            print(f'Name = {product_name}')
            print(f'Price = {max_price}')
            print("*" * 20)

    @staticmethod
    def delete_product_by_id(product_id):
        arr_products = []
        with open("purchases.txt", 'r') as file:
            for line in file:
                arr_products.append(line)

            for item in arr_products:
                if product_id == item[0]:
                    arr_products.pop(arr_products.index(item))
        with open("purchases.txt", 'w') as file:
            for item in arr_products:
                file.write(item)


while True:
    print("\n1 - Add purchase to book")
    print("2 - Search purchase")
    print("3 - Show the most expensive purchase")
    print("4 - Delete purchase from the book")
    print("5 - Exit")

    choice = input("\nEnter your choice(number) : ")
    match choice:
        case '1':
            id = input("id = ")
            name = input("name = ")
            price = input("price = ")

            purchase = Purchase(id, name, price)
            purchase.add_purchase()

        case '2':
            print("1 - id")
            print("2 - name")
            print("3 - price")
            search = input("Which feature do you want to search for? (press number) : ")

            match search:
                case '1':
                    search_item = input("Your search id = ")
                    purchase = Purchase(0, 0, 0)
                    purchase.search_product('id', search_item)
                case '2':
                    search_item = input("Your search name = ")
                    purchase = Purchase(0, 0, 0)
                    purchase.search_product('name', search_item)
                case '3':
                    search_item = input("Your search price = ")
                    purchase = Purchase(0, 0, 0)
                    purchase.search_product('price', search_item)

        case '3':
            purchase = Purchase(0, 0, 0)
            purchase.most_expensive_product()

        case '4':
            delete_id = input("Enter your delete product id : ")

            purchase = Purchase(0, 0, 0)
            purchase.delete_product_by_id(delete_id)

        case '5':
            exit()
