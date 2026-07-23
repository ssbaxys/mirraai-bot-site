import random
import time
import sys

# --- Конфигурация игрока ---
player = {
    "name": "Герой",
    "hp": 100,
    "gold": 0,
    "potions": 2,
    "weapon": "Ржавый меч"
}

# --- Вспомогательные функции ---

def print_slow(text):
    """Выводит текст по буквам для атмосферности."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)  # Скорость печати
    print()

def show_stats():
    """Показывает текущее состояние игрока."""
    print("\n" + "="*30)
    print(f"Имя: {player['name']}")
    print(f"Здоровье: {player['hp']} HP")
    print(f"Золото: {player['gold']}")
    print(f"Зелья: {player['potions']}")
    print(f"Оружие: {player['weapon']}")
    print("="*30 + "\n")

def get_input(options):
    """Безопасный ввод данных от пользователя."""
    while True:
        choice = input(f"Ваш выбор ({'/'.join(options)}): ").lower()
        if choice in options:
            return choice
        print("Неверная команда, попробуйте снова.")

# --- Игровые события ---

def battle():
    """Логика сражения с монстром."""
    monster_hp = random.randint(20, 50)
    print_slow(f"!!! ВНЕЗАПНО! Появляется Скелет ({monster_hp} HP) !!!")

    while monster_hp > 0 and player["hp"] > 0:
        action = get_input(["а", "з"]) # а - атака, з - зелье
        
        if action == "а":
            damage = random.randint(10, 25)
            monster_hp -= damage
            print(f"Вы ударили скелета на {damage} урона.")
        elif action == "з":
            if player["potions"] > 0:
                player["hp"] += 30
                player["potions"] -= 1
                print("Вы выпили зелье. Здоровье восстановлено.")
            else:
                print("У вас нет зелий!")
                continue # Пропуск хода врага, если зелья не было

        # Ответный удар монстра
        if monster_hp > 0:
            enemy_dmg = random.randint(5, 15)
            player["hp"] -= enemy_dmg
            print(f"Скелет бьет вас! Вы теряете {enemy_dmg} HP.")
            print(f"Ваше здоровье: {player['hp']}")

    if player["hp"] > 0:
        loot = random.randint(10, 50)
        player["gold"] += loot
        print_slow(f"Победа! Вы нашли {loot} золотых монет.")
    else:
        print_slow("Вы пали в бою...")
        sys.exit()

def chest():
    """Событие: нахождение сундука."""
    print_slow("Вы видите старый сундук в углу комнаты.")
    choice = get_input(["о", "у"]) # о - открыть, у - уйти

    if choice == "о":
        if random.random() > 0.3:
            gold = random.randint(50, 100)
            player["gold"] += gold
            print_slow(f"Удача! В сундуке было {gold} монет!")
        else:
            print_slow("Это ловушка! Из сундука вырвался ядовитый газ.")
            player["hp"] -= 15
    else:
        print_slow("Вы решили не рисковать и прошли мимо.")

def shop():
    """Событие: бродячий торговец."""
    print_slow("Встретился торговец. 'Хочешь зелье за 50 монет?'")
    if player["gold"] >= 50:
        choice = get_input(["д", "н"])
        if choice == "д":
            player["gold"] -= 50
            player["potions"] += 1
            print("Вы купили лечебное зелье.")
        else:
            print("Вы отказались от покупки.")
    else:
        print("У вас недостаточно золота.")

# --- Основной цикл игры ---

def main():
    print_slow("Добро пожаловать в Текстовое Подземелье!")
    player["name"] = input("Как зовут героя? ")
    
    rooms_cleared = 0
    
    while player["hp"] > 0:
        show_stats()
        print_slow(f"Вы входите в комнату №{rooms_cleared + 1}...")
        time.sleep(1)

        # Случайный выбор события
        event = random.randint(1, 3)
        
        if event == 1:
            battle()
        elif event == 2:
            chest()
        elif event == 3:
            shop()
        
        print("\nЧто делаем дальше?")
        choice = get_input(["и", "в"]) # и - идти дальше, в - выход
        
        if choice == "в":
            print("Вы сбежали из подземелья с награбленным!")
            break
            
        rooms_cleared += 1
        
        if rooms_cleared == 10:
            print_slow("\n*** ПОЗДРАВЛЯЕМ! ВЫ ПРОШЛИ ПОДЗЕМЕЛЬЕ! ***")
            break

    print(f"\nИгра окончена. Итоговое золото: {player['gold']}")

if __name__ == "__main__":
    main()