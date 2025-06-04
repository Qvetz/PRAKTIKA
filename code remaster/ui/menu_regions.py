from models.region import Region, get_all_regions, get_region_by_id

def menu_regions():
    while True:
        print("\n=== Управление регионами ===")
        print("1. Показать все регионы")
        print("2. Добавить регион")
        print("3. Удалить регион")
        print("4. Изменить регион")
        print("0. Назад в главное меню")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            regions = get_all_regions()
            print("\nСписок регионов:")
            for r in regions:
                print(f"{r.id}. {r.name}")
                
        elif choice == "2":
            print("\n=== Добавление нового региона ===")
            name = input("Название региона: ")
            region = Region(name=name)
            region.save()
            print("✅ Регион добавлен.")
            
        elif choice == "3":
            region_id = input("Введите ID региона для удаления: ")
            region = Region(id=int(region_id))
            region.delete()
            print("✅ Регион удалён.")
            
        elif choice == "4":
            region_id = input("Введите ID региона для редактирования: ")
            region = get_region_by_id(int(region_id))
            if not region:
                print("❌ Регион не найден!")
                continue
                
            new_name = input(f"Новое название (текущее: {region.name}): ")
            if new_name:
                region.name = new_name
                region.save()
                print("✅ Регион обновлён.")
                
        elif choice == "0":
            break
            
        else:
            print("❌ Неверный ввод.")