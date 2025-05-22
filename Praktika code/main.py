from Models.client import Client
from database import transportation_db
from Models.sale import Sale
from Models.gruz import Gruz
from Models.city import City
from Models.adress import Adress

def show_main_menu():
    while True:
        print("\n Грузовые перевозки 'Фурри компани'")
        print("1. Работа с клиентами")
        print("2. Работа с грузами")
        print("3. Заказы")
        print("0. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            client_menu()
        elif choice == "2":
            gruz_menu()
        elif choice == "3":
            sale_menu()
        elif choice == "0":
            break
        else:
            print("Неверный выбор")

def client_menu():
    while True:
        print("\n Работа с клиентами")
        print("1. Добавить клиента")
        print("2. Просмотреть клиентов")
        print("0. Назад")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            surname = input("Фамилия: ")
            name = input("Имя: ")
            patronymic = input("Отчество: ")
            address = input("Адрес: ")
            phone = input("Телефон: ")
            
            client = Client(surname=surname, name=name, patronymic=patronymic, address=address, phone=phone)
            client.save()
            print("Клиент сохранен!")
            
        elif choice == "2":
            clients = Client.get_all()
            print("\nСписок клиентов:")
            for c in clients:
                print(f"{c.id}. {c.surname} {c.name} {c.patronymic}")
        elif choice == "0":
            break

def gruz_menu():
    while True:
        print("\n Работа с грузами")
        print("1. Добавить город")
        print("2. Добавить адрес")
        print("3. Добавить груз")
        print("4. Просмотреть грузы")
        print("0. Назад")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            name = input("Название города: ")
            region = input("Регион: ")
            
            city = City(name=name, region=region)
            city.save()
            print("Город добавлен!")
            
        elif choice == "2":
            street_address = input("Адрес: ")
            cities = City.get_all()
            for c in cities:
                print(f"{c.id}. {c.name}")
            city_id = int(input("ID города: "))
            
            address = Adress(address=street_address, city_id=city_id)
            address.save()
            print("Адрес добавлен!")
            
        elif choice == "3":
            duration = int(input("Длительность (дни): "))
            price = float(input("Базовая цена: "))
            
            addresses = Adress.get_all()
            for a in addresses:
                city = City.get_by_id(a.city_id)
                if city:
                    print(f"{a.id}. {city.name}, {a.address}")
                else:
                    print(f"{a.id}. [НЕИЗВЕСТНЫЙ ГОРОД], {a.address}")

            address_id = int(input("ID адреса: "))
            
            gruz = Gruz(duration=duration, base_price=price, adress_id=address_id)
            gruz.save()
            print("Груз добавлен!")
            
        elif choice == "4":
            gruzs = Gruz.get_all()
            for g in gruzs:
                address = Adress.get_by_id(g.adress_id)
                city = City.get_by_id(address.city_id)
                print(f"{g.id}. {city.name} - {address.address} ({g.duration} дней, {g.base_price} руб.)")
                
        elif choice == "0":
            break

def sale_menu():
    while True:
        print("\n Заказы")
        print("1. Оформить заказ")
        print("2. Просмотреть заказы")
        print("0. Назад")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            # Выбор клиента
            clients = Client.get_all()
            for c in clients:
                print(f"{c.id}. {c.surname} {c.name} {c.patronymic}")
            client_id = int(input("ID клиента: "))
            
            # Выбор груза
            gruzs = Gruz.get_all()
            for g in gruzs:
                address = Adress.get_by_id(g.adress_id)
                city = City.get_by_id(address.city_id)
                print(f"{g.id}. {city.name} - {address.address} ({g.duration} дней, {g.base_price} руб.)")
            gruz_id = int(input("ID груза: "))
            
            # Скидки
            print("Доступные скидки:")
            print("- 5% как за постоянного клиента")
            discount = float(input("Общий процент скидки: "))
            departure = input("Дата выезда (ГГГГ-ММ-ДД): ")
            
            sale = Sale(
                client_id=client_id,
                gruz_id=gruz_id,
                discount=discount,
                departure_date=departure
            )
            sale.save()
            print(f"Заказ оформлен! Итоговая цена: {sale.total_price} руб.")
            
        elif choice == "2":
            sales = Sale.get_all()
            for s in sales:
                client = Client.get_by_id(s.client_id)
                gruz = Gruz.get_by_id(s.gruz_id)
                address = Adress.get_by_id(gruz.adress_id)
                city = City.get_by_id(address.city_id)
                print(f"{s.id}. {client.surname} {client.name} - {city.name} ({gruz.duration} дней), {s.total_price} руб.")
                
        elif choice == "0":
            break

if __name__ == '__main__':
    transportation_db()
    show_main_menu()
