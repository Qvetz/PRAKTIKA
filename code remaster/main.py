from database.db_manager import initialize_db
from ui.main_menu import show_main_menu
from ui.menu_regions import menu_regions
from ui.menu_cities import menu_cities
from ui.menu_addresses import menu_addresses
from ui.menu_clients import menu_clients
from ui.menu_cargo import menu_cargo
from ui.menu_orders import menu_orders

def main():
    # Инициализация базы данных
    initialize_db()
    
    print("=== Система управления грузоперевозками ===")
    print("Добро пожаловать в систему учета заказов на перевозку грузов!")
    
    while True:
        user_choice = show_main_menu()
        
        if user_choice == "1":
            menu_regions()
        elif user_choice == "2":
            menu_cities()
        elif user_choice == "3":
            menu_addresses()
        elif user_choice == "4":
            menu_clients()
        elif user_choice == "5":
            menu_cargo()
        elif user_choice == "6":
            menu_orders()
        elif user_choice == "0":
            print("\nСпасибо за использование системы. До свидания!")
            break
        else:
            print("\n❌ Неверный ввод. Пожалуйста, выберите действие из меню.")

if __name__ == "__main__":
    main()