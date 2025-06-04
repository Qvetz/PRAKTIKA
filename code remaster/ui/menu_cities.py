from models.city import City, get_all_cities, get_city_by_id
from models.region import get_all_regions

def menu_cities():
    while True:
        print("\n=== Управление городами ===")
        print("1. Показать все города")
        print("2. Добавить город")
        print("3. Удалить город")
        print("4. Изменить город")
        print("0. Назад в главное меню")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            cities = get_all_cities()
            print("\nСписок городов:")
            for c in cities:
                print(f"{c.id}. {c.name} (регион ID: {c.region_id})")
                
        elif choice == "2":
            print("\n=== Добавление нового города ===")
            name = input("Название города: ")
            
            print("\nДоступные регионы (ID - Название):")
            regions = get_all_regions()
            for r in regions:
                print(f"{r.id} - {r.name}")
                
            region_id = int(input("ID региона: "))
            city = City(name=name, region_id=region_id)
            city.save()
            print("✅ Город добавлен.")
            
        elif choice == "3":
            city_id = input("Введите ID города для удаления: ")
            city = City(id=int(city_id))
            city.delete()
            print("✅ Город удалён.")
            
        elif choice == "4":
            city_id = input("Введите ID города для редактирования: ")
            city = get_city_by_id(int(city_id))
            if not city:
                print("❌ Город не найден!")
                continue
                
            new_name = input(f"Новое название (текущее: {city.name}): ")
            if new_name:
                city.name = new_name
                
            print("\nТекущий регион ID:", city.region_id)
            print("Доступные регионы (ID - Название):")
            regions = get_all_regions()
            for r in regions:
                print(f"{r.id} - {r.name}")
                
            new_region_id = input("Новый ID региона (оставьте пустым, чтобы не менять): ")
            if new_region_id:
                city.region_id = int(new_region_id)
                
            city.save()
            print("✅ Город обновлён.")
            
        elif choice == "0":
            break
            
        else:
            print("❌ Неверный ввод.")