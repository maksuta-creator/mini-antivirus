# main.py
# Универсальный каркас консольного проекта

from cmath import e
from inspect import signature
import os


def print_header(title: str) -> None:
    print("\n" + "=" * 50)
    print(title)
    print("=" * 50)

def read_int(prompt: str) -> int:
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            return int(s)
        print("Ошибка: введите целое число.")

def read_float(prompt: str) -> float:
    while True:
        s = input(prompt).strip().replace(",", ".")
        try:
            return float(s)
        except ValueError:
            print("Ошибка: введите число (например 10 или 10.5).")

def pause() -> None:
    input("\nНажмите Enter, чтобы продолжить...")


# ---- Здесь будут функции проекта ----


"=================================================================================="
def action_1():
    print_header("Проверка файла по сигнатурам")


    signature_filename = "signatures.txt"
    if not os.path.exists(signature_filename):
        print(f"Ошибка: Файл сигнатур '{signature_filename}' не найден по пути: {os.path.abspath(signature_filename)}") # ищет путь к файлу
        pause()


    def load_signatures(filename="signatures.txt"):                         #загрузка сигнатур 47-56
        try:
            with open(filename, "r", encoding="utf-8") as f:
                return [line.strip() for line in f]
        except FileNotFoundError:
            print(f"Ошибка: Файл сигнатур '{filename}' не найден.")
            return []
        except Exception as e:
            print(f"Ошибка при загрузке сигнатур: {e}")
            return []

    signatures = load_signatures()
    if not signatures:
        print("Не удалось загрузить сигнатуры. Проверка невозможна.")       
        pause()  
        return

    try:
        with open("тест.txt", "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        print("Ошибка: Файл 'тест.txt' не найден.")
        pause()
        return
    except Exception as e:
        print(f"Ошибка при чтении файла 'тест.txt': {e}")
        pause()
        return

    # Проверка файла по сигнатурам
    dangerous = False
    for signature in signatures:
        if signature in content:
            dangerous = True
            print(f"Обнаружена опасная сигнатура: {signature}")
            break  # Прекращаем проверку, если найдена хотя бы одна сигнатура

    if dangerous:
        print("Файл 'тест.txt' **ОПАСЕН**! Обнаружены вредоносные сигнатуры.")
    else:
        print("Файл 'тест.txt' выглядит **БЕЗОПАСНЫМ**. Опасные сигнатуры не обнаружены.")

    pause()

"=================================================================================="



def action_2():
    print_header("Функция 2")
    print("Здесь будет логика. Пока заглушка.")
    pause()

def action_3():
    print_header("Функция 3")
    print("Здесь будет логика. Пока заглушка.")
    pause()

def show_menu() -> None:
    print("\nВыберите действие:")
    print("1) Действие 1")
    print("2) Действие 2")
    print("3) Действие 3")
    print("0) Выход")

def main():
    print_header("Мой индивидуальный проект")

    while True:
        show_menu()
        choice = input("Ваш выбор: ").strip()

        if choice == "1":
            action_1()
        elif choice == "2":
            action_2()
        elif choice == "3":
            action_3()
        elif choice == "0":
            print("\nВыход. Пока!")
            break
        else:
            print("Ошибка: выберите пункт из меню (0–3).")

if __name__ == "__main__":
    main()

