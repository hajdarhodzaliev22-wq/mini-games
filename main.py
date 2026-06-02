import random
import time
import os

# --- Очистка экрана для красоты ---
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# ================= ИГРА 1: УГАДАЙ ЧИСЛО =================
def game_guess_number():
    clear_screen()
    print("🎯 ИГРА 1: Угадай число")
    print("-" * 30)
    
    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print(f"Я загадал число от 1 до 100. У тебя {max_attempts} попыток.")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"\nПопытка {attempts + 1}/{max_attempts}: "))
            attempts += 1
            
            if guess < number:
                print("⬆️ Больше!")
            elif guess > number:
                print("⬇️ Меньше!")
            else:
                print(f"\n🎉 Победа! Ты угадал число {number} за {attempts} попыток!")
                input("\nНажми Enter для выхода...")
                return
                
        except ValueError:
            print("❌ Введите целое число!")
            
    print(f"\n😢 Попытки кончились. Загаданное число было: {number}")
    input("\nНажми Enter для выхода...")

# ================= ИГРА 2: КАМЕНЬ, НОЖНИЦЫ, БУМАГА =================
def game_rps():
    clear_screen()
    print("✂️ ИГРА 2: Камень, Ножницы, Бумага")
    print("-" * 30)
    
    choices = ["камень", "ножницы", "бумага"]
    player_score = 0
    computer_score = 0
        while True:
        print(f"\nСчёт: Игрок {player_score} - {computer_score} Комп")
        print("1. Камень\n2. Ножницы\n3. Бумага\n0. Выход")
        
        choice = input("Твой выбор: ")
        if choice == '0':
            break
        if choice not in ['1', '2', '3']:
            print("Неверный ввод!")
            continue
            
        player_choice = choices[int(choice) - 1]
        computer_choice = random.choice(choices)
        
        print(f"Ты: {player_choice} | Комп: {computer_choice}")
        
        if player_choice == computer_choice:
            print("🤝 Ничья!")
        elif (player_choice == "камень" and computer_choice == "ножницы") or \
             (player_choice == "ножницы" and computer_choice == "бумага") or \
             (player_choice == "бумага" and computer_choice == "камень"):
            print("✅ Ты выиграл раунд!")
            player_score += 1
        else:
            print("❌ Компьютер выиграл раунд!")
            computer_score += 1
            
    print("Спасибо за игру!")
    input("\nНажми Enter для выхода...")

# ================= ИГРА 3: ВИКТОРИНА =================
def game_quiz():
    clear_screen()
    print("🧠 ИГРА 3: Викторина")
    print("-" * 30)
    
    questions = [
        {"q": "Столица Франции?", "a": "Париж", "opts": ["Лондон", "Берлин", "Париж", "Мадрид"]},
        {"q": "Сколько ног у паука?", "a": "8", "opts": ["6", "8", "10", "4"]},
        {"q": "Язык этого проекта?", "a": "Python", "opts": ["Java", "C++", "Python", "HTML"]},
        {"q": "2 + 2 * 2 = ?", "a": "6", "opts": ["8", "6", "4", "10"]}
    ]
    
    score = 0
    for i, q in enumerate(questions):
        print(f"\nВопрос {i+1}: {q['q']}")
        for j, opt in enumerate(q['opts']):
            print(f"{j+1}. {opt}")
        
        ans = input("Ответ (номер): ")        if ans.isdigit() and 1 <= int(ans) <= 4:
            if q['opts'][int(ans)-1] == q['a']:
                print("✅ Верно!")
                score += 1
            else:
                print(f"❌ Неверно. Правильный ответ: {q['a']}")
        else:
            print("❌ Неверный ввод.")
            
    print(f"\n🏁 Итог: {score} из {len(questions)} правильных ответов.")
    input("\nНажми Enter для выхода...")

# ================= ИГРА 4: КРЕСТИКИ-НОЛИКИ =================
def game_tic_tac_toe():
    clear_screen()
    print("❌⭕ ИГРА 4: Крестики-нолики")
    print("-" * 30)
    
    board = [" " for _ in range(9)]
    
    def print_board():
        print(f" {board[0]} | {board[1]} | {board[2]} ")
        print("---+---+---")
        print(f" {board[3]} | {board[4]} | {board[5]} ")
        print("---+---+---")
        print(f" {board[6]} | {board[7]} | {board[8]} ")

    def check_win(player):
        wins = [(0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6)]
        return any(all(board[i] == player for i in combo) for combo in wins)

    current_player = "X"
    for turn in range(9):
        print_board()
        try:
            move = int(input(f"Ход игрока {current_player} (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = current_player
                if check_win(current_player):
                    print_board()
                    print(f"🎉 Игрок {current_player} победил!")
                    input("\nНажми Enter для выхода...")
                    return
                current_player = "O" if current_player == "X" else "X"
            else:
                print("❌ Сюда ходить нельзя!")
        except ValueError:
            print("❌ Введите число!")
            
    print_board()    print("🤝 Ничья!")
    input("\nНажми Enter для выхода...")

# ================= ИГРА 5: ВИСЕЛИЦА =================
def game_hangman():
    clear_screen()
    print("💀 ИГРА 5: Виселица")
    print("-" * 30)
    
    words = ["python", "github", "code", "game", "hello", "world"]
    word = random.choice(words)
    guessed = ["_"] * len(word)
    lives = 6
    
    while lives > 0 and "_" in guessed:
        print(f"\nСлово: {' '.join(guessed)}")
        print(f"Жизни: {'❤️' * lives}")
        letter = input("Введи букву: ").lower()
        
        if len(letter) != 1 or not letter.isalpha():
            print("❌ Введи одну букву!")
            continue
            
        if letter in word:
            for i, char in enumerate(word):
                if char == letter:
                    guessed[i] = letter
            print("✅ Есть такая буква!")
        else:
            lives -= 1
            print("❌ Нет такой буквы!")
            
    if "_" not in guessed:
        print(f"\n🎉 Победа! Слово: {word}")
    else:
        print(f"\n😢 Проигрыш. Слово было: {word}")
        
    input("\nНажми Enter для выхода...")

# ================= ИГРА 6: КОСТИ =================
def game_dice():
    clear_screen()
    print("🎲 ИГРА 6: Бросок кубика")
    print("-" * 30)
    
    while True:
        input("\nНажми Enter, чтобы бросить кубик...")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
                print(f"\n🎲 Кубик 1: [{dice1}]")
        print(f"🎲 Кубик 2: [{dice2}]")
        print(f"✨ Сумма: {dice1 + dice2}")
        
        again = input("\nБросить еще? (y/n): ").lower()
        if again != 'y':
            break
            
    input("\nНажми Enter для выхода...")

# ================= ГЛАВНОЕ МЕНЮ =================
def main_menu():
    while True:
        clear_screen()
        print("=" * 40)
        print("   🎮 МИНИ-ИГРЫ НА PYTHON")
        print("   Автор: Хайдар | Год: 2026")
        print("=" * 40)
        print("1. Угадай число")
        print("2. Камень, Ножницы, Бумага")
        print("3. Викторина")
        print("4. Крестики-нолики")
        print("5. Виселица")
        print("6. Бросок кубика")
        print("0. Выход")
        print("-" * 40)
        
        choice = input("Выбери игру (0-6): ")
        
        if choice == '1': game_guess_number()
        elif choice == '2': game_rps()
        elif choice == '3': game_quiz()
        elif choice == '4': game_tic_tac_toe()
        elif choice == '5': game_hangman()
        elif choice == '6': game_dice()
        elif choice == '0': 
            print("Пока! 👋")
            break
        else:
            print("❌ Неверный выбор!")
            time.sleep(1)

if __name__ == "__main__":
    main_menu()