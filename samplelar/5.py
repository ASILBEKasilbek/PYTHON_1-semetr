import os
import random
import time
import shutil

# Ranglarni o'zgartirish uchun funksiya
def green_text(text):
    return f"\033[32m{text}\033[0m"

# Tasodifiy so'zlar ro'yxati
words = ["hello", "world", "matrix", "python", "code", "random", "words", "effect", "green", "falling", "text"]

# Terminal o'lchamini olish
columns, rows = shutil.get_terminal_size()

# Terminalni tozalash
os.system('cls' if os.name == 'nt' else 'clear')

try:
    # Boshlang'ich qatorlar
    matrix = [' ' * columns for _ in range(rows)]

    # Har bir kolonka uchun boshlang'ich pozitsiyalar
    positions = [random.randint(0, rows - 1) for _ in range(columns)]

    while True:
        # Har bir kolonka uchun yangilanish
        for col in range(columns):
            # Tasodifiy so'z tanlash
            word = random.choice(words)
            word_length = len(word)

            # So'zning boshlanish pozitsiyasini yangilash
            pos = positions[col]

            # Qatorlarni yangilash
            for i in range(word_length):
                if 0 <= pos + i < rows:
                    row = matrix[pos + i]
                    matrix[pos + i] = row[:col] + green_text(word[i]) + row[col + 1:]

            # Pozitsiyani yangilash
            positions[col] = (pos + 1) % rows

        # Terminalni tozalash va yangilangan qatorlarni chiqarish
        os.system('cls' if os.name == 'nt' else 'clear')
        for line in matrix:
            print(line)

        # Keyingi yangilanishdan oldin kutish
        time.sleep(0.1)
except KeyboardInterrupt:
    # Foydalanuvchi Ctrl+C bosganida chiqish
    print("\nMatrix effekti to'xtatildi.")
