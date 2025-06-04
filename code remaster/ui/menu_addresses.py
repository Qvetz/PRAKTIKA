from models.address import Address, get_all_addresses, get_address_by_id
from models.city import get_all_cities

def menu_addresses():
    while True:
        print("\n=== Управление адресами ===")
        print("1. Показать все адреса")
        print("2. Добавить адрес")
        print("3. Удалить адрес")
        print("4. Изменить адрес")
        print("0. Назад в главное меню")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            addresses = get_all_addresses()
            print("\nСписок адресов:")
            for a in addresses:
                print(f"{a.id}. г.{a.city_id}, ул.{a.street}, д.{a.building}, кв.{a.apartment}")
                
        elif choice == "2":
            print("\n=== Добавление нового адреса ===")
            
            print("\nДоступные города (ID):")
            cities = get_all_cities()
            for c in cities:
                print(f"{c.id} - {c.name}")
                
            city_id = int(input("ID города: "))
            street = input("Улица: ")
            building = input("Дом: ")
            apartment = input("Квартира (необязательно): ")
            
            address = Address(city_id=city_id, street=street, building=building, apartment=apartment)
            address.save()
            print("✅ Адрес добавлен.")
            
        elif choice == "3":
            address_id = input("Введите ID адреса для удаления: ")
            address = Address(id=int(address_id))
            address.delete()
            print("✅ Адрес удалён.")
            
        elif choice == "4":
            address_id = input("Введите ID адреса для редактирования: ")
            address = get_address_by_id(int(address_id))
            if not address:
                print("❌ Адрес не найден!")
                continue
                
            print("\nТекущий город ID:", address.city_id)
            print("Доступные города (ID - Название):")
            cities = get_all_cities()
            for c in cities:
                print(f"{c.id} - {c.name}")
                
            new_city_id = input("Новый ID города (оставьте пустым, чтобы не менять): ")
            if new_city_id:
                address.city_id = int(new_city_id)
                
            new_street = input(f"Новая улица (текущая: {address.street}): ")
            if new_street:
                address.street = new_street
                
            new_building = input(f"Новый дом (текущий: {address.building}): ")
            if new_building:
                address.building = new_building
                
            new_apartment = input(f"Новая квартира (текущая: {address.apartment}): ")
            if new_apartment:
                address.apartment = new_apartment
                
            address.save()
            print("✅ Адрес обновлён.")
            
        elif choice == "0":
            break
            
        else:
            print("❌ Неверный ввод.")