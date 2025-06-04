from models.order import Order, get_all_orders, get_order_by_id
from models.client import get_all_clients
from models.cargo import get_all_cargo
from models.address import get_all_addresses
from datetime import datetime

def menu_orders():
    while True:
        print("\n=== Управление заказами ===")
        print("1. Показать все заказы")
        print("2. Добавить заказ")
        print("3. Удалить заказ")
        print("4. Изменить заказ")
        print("5. Показать заказы по дате")
        print("0. Назад в главное меню")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            orders = get_all_orders()
            print("\nСписок заказов:")
            for o in orders:
                print(f"{o.id}. Клиент ID: {o.client_id} | Груз ID: {o.cargo_id} | "
                      f"От: {o.from_address_id} -> До: {o.to_address_id} | "
                      f"Дата: {o.order_date} | Доставка: {o.delivery_date} | "
                      f"Цена: {o.price} (скидка {o.discount}%) | Статус: {o.status}")
                      
        elif choice == "2":
            print("\n=== Добавление нового заказа ===")
            
            print("\nДоступные клиенты (ID - Фамилия Имя):")
            clients = get_all_clients()
            for c in clients:
                print(f"{c.id} - {c.surname} {c.name}")
            client_id = int(input("ID клиента: "))
            
            print("\nДоступные грузы (ID - Описание):")
            cargo_list = get_all_cargo()
            for c in cargo_list:
                print(f"{c.id} - {c.description}")
            cargo_id = int(input("ID груза: "))
            
            print("\nДоступные адреса отправления (ID):")
            addresses = get_all_addresses()
            for a in addresses:
                print(f"{a.id}. г.{a.city_id}, ул.{a.street}, д.{a.building}")
            from_address_id = int(input("ID адреса отправления: "))
            
            print("\nДоступные адреса доставки (ID):")
            for a in addresses:
                print(f"{a.id}. г.{a.city_id}, ул.{a.street}, д.{a.building}")
            to_address_id = int(input("ID адреса доставки: "))
            
            order_date = input("Дата заказа (ГГГГ-ММ-ДД, пусто - сегодня): ") or datetime.now().strftime("%Y-%m-%d")
            delivery_date = input("Дата доставки (ГГГГ-ММ-ДД): ")
            price = float(input("Цена: "))
            status = input("Статус (new/in_progress/delivered/canceled): ") or "new"
            
            order = Order(
                client_id=client_id,
                cargo_id=cargo_id,
                from_address_id=from_address_id,
                to_address_id=to_address_id,
                order_date=order_date,
                delivery_date=delivery_date,
                price=price,
                status=status
            )
            order.save()
            print("✅ Заказ добавлен.")
            
        elif choice == "3":
            order_id = input("Введите ID заказа для удаления: ")
            order = Order(id=int(order_id))
            order.delete()
            print("✅ Заказ удалён.")
            
        elif choice == "4":
            order_id = input("Введите ID заказа для редактирования: ")
            order = get_order_by_id(int(order_id))
            if not order:
                print("❌ Заказ не найден!")
                continue
                
            print("\nТекущий клиент ID:", order.client_id)
            print("Доступные клиенты (ID - Фамилия Имя):")
            clients = get_all_clients()