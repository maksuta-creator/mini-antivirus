import os

SIGNATURE_FILE = "signatures.txt"

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

def load_signatures(filename=SIGNATURE_FILE):
    """Загружает сигнатуры из файла, игнорируя пустые строки."""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Ошибка: Файл сигнатур '{filename}' не найден.")
        return []
    except Exception as e:
        print(f"Ошибка при загрузке сигнатур: {e}")
        return []

def check_file_against_signatures(filepath, signatures):
    """
    Проверяет файл на наличие сигнатур.
    Сначала пробует текстовый режим (UTF-8), при ошибке — бинарный.
    Возвращает список найденных сигнатур.
    """
    # Пробуем текстовый режим
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        return [sig for sig in signatures if sig in content]
    except UnicodeDecodeError:
        # Бинарный режим
        with open(filepath, "rb") as f:
            content = f.read()
        found = []
        for sig in signatures:
            try:
                sig_bytes = sig.encode('utf-8')
                if sig_bytes in content:
                    found.append(sig)
            except:
                continue
        return found
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None

def action_1():
    print_header("Проверка файла по сигнатурам")
    signatures = load_signatures()
    if not signatures:
        print("Не удалось загрузить сигнатуры. Проверка невозможна.")
        pause()
        return

    filename = input("Введите имя файла для проверки: ").strip()
    if not filename:
        print("Имя файла не может быть пустым.")
        pause()
        return

    found = check_file_against_signatures(filename, signatures)
    if found is None:
        print("Не удалось прочитать файл.")
    elif found:
        print(f"Файл '{filename}' **ОПАСЕН**! Обнаружены сигнатуры:")
        for sig in found:
            print(f"  - {sig}")
    else:
        print(f"Файл '{filename}' выглядит **БЕЗОПАСНЫМ**.")
    pause()

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
    print("1) Проверка файла по сигнатурам")
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
