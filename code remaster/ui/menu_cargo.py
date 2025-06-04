from models.cargo import Cargo, get_all_cargo, get_cargo_by_id

def menu_cargo():
    while True:
        print("\n=== Управление грузами ===")
        print("1. Показать все грузы")
        print("2. Добавить груз")
        print("3. Удалить груз")
        print("4. Изменить груз")
        print("0. Назад в главное меню")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            cargo_list = get_all_cargo()
            print("\nСписок грузов:")
            for c in cargo_list:
                print(f"{c.id}. {c.description} | Вес: {c.weight} кг | Объем: {c.volume} м³")
                if c.special_conditions:
                    print(f"   Особые условия: {c.special_conditions}")
                    
        elif choice == "2":
            print("\n=== Добавление нового груза ===")
            description = input("Описание груза: ")
            weight = float(input("Вес (кг): "))
            volume = float(input("Объем (м³): "))
            special_conditions = input("Особые условия (необязательно): ")
            
            cargo = Cargo(description=description, weight=weight, volume=volume, 
                        special_conditions=special_conditions or None)
            cargo.save()
            print("✅ Груз добавлен.")
            
        elif choice == "3":
            cargo_id = input("Введите ID груза для удаления: ")
            cargo = Cargo(id=int(cargo_id))
            cargo.delete()
            print("✅ Груз удалён.")
            
        elif choice == "4":
            cargo_id = input("Введите ID груза для редактирования: ")
            cargo = get_cargo_by_id(int(cargo_id))
            if not cargo:
                print("❌ Груз не найден!")
                continue
                
            new_description = input(f"Новое описание (текущее: {cargo.description}): ")
            if new_description:
                cargo.description = new_description
                
            new_weight = input(f"Новый вес (текущий: {cargo.weight} кг): ")
            if new_weight:
                cargo.weight = float(new_weight)
                
            new_volume = input(f"Новый объем (текущий: {cargo.volume} м³): ")
            if new_volume:
                cargo.volume = float(new_volume)
                
            new_conditions = input(f"Новые условия (текущие: {cargo.special_conditions or 'нет'}): ")
            if new_conditions:
                cargo.special_conditions = new_conditions
                
            cargo.save()
            print("✅ Груз обновлён.")
            
        elif choice == "0":
            break
            
        else:
            print("❌ Неверный ввод.")