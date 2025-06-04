from models.client import Client, get_all_clients, get_client_by_id

def menu_clients():
    while True:
        print("\n=== Управление клиентами ===")
        print("1. Показать всех клиентов")
        print("2. Добавить клиента")
        print("3. Удалить клиента")
        print("4. Изменить клиента")
        print("5. Сделать клиента постоянным")
        print("0. Назад в главное меню")
        
        choice = input("Выберите действие: ")
        
        if choice == "1":
            clients = get_all_clients()
            print("\nСписок клиентов:")
            for c in clients:
                status = "постоянный" if c.is_regular else "разовый"
                print(f"{c.id}. {c.surname} {c.name} {c.patronymic or ''}, тел.: {c.phone} ({status})")
                
        elif choice == "2":
            print("\n=== Добавление нового клиента ===")
            surname = input("Фамилия: ")
            name = input("Имя: ")
            patronymic = input("Отчество (необязательно): ")
            phone = input("Телефон: ")
            is_regular = input("Постоянный клиент? (y/n): ").lower() == 'y'
            
            client = Client(surname=surname, name=name, patronymic=patronymic, 
                          phone=phone, is_regular=is_regular)
            client.save()
            print("✅ Клиент добавлен.")
            
        elif choice == "3":
            client_id = input("Введите ID клиента для удаления: ")
            client = Client(id=int(client_id))
            client.delete()
            print("✅ Клиент удалён.")
            
        elif choice == "4":
            client_id = input("Введите ID клиента для редактирования: ")
            client = get_client_by_id(int(client_id))
            if not client:
                print("❌ Клиент не найден!")
                continue
                
            new_surname = input(f"Новая фамилия (текущая: {client.surname}): ")
            if new_surname:
                client.surname = new_surname
                
            new_name = input(f"Новое имя (текущее: {client.name}): ")
            if new_name:
                client.name = new_name
                
            new_patronymic = input(f"Новое отчество (текущее: {client.patronymic or 'нет'}): ")
            if new_patronymic:
                client.patronymic = new_patronymic
                
            new_phone = input(f"Новый телефон (текущий: {client.phone}): ")
            if new_phone:
                client.phone = new_phone
                
            client.save()
            print("✅ Клиент обновлён.")
            
        elif choice == "5":
            client_id = input("Введите ID клиента для изменения статуса: ")
            client = get_client_by_id(int(client_id))
            if not client:
                print("❌ Клиент не найден!")
                continue
                
            client.is_regular = not client.is_regular
            status = "теперь постоянный" if client.is_regular else "больше не постоянный"
            client.save()
            print(f"✅ Клиент {status}.")
            
        elif choice == "0":
            break
            
        else:
            print("❌ Неверный ввод.")