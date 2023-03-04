from Ciphers import CAESAR, TRITEMIUS


def create_file():
    filename = input("Введіть ім'я файлу: ")
    with open(filename, 'w') as file:
        print("Файл %s створено успішно!" % file.name)


def open_file():
    filename = input("Введіть ім'я файлу: ")
    with open(filename, 'r') as file:
        print(file.read())


def save_file():
    filename = input("Введіть ім'я файлу: ")
    content = input("Введіть текст для збереження: ")
    with open(filename, 'w') as file:
        file.write(content)
        print("Файл збережено успішно!")


def print_file():
    # import os
    # filename = input("Введіть ім'я файлу: ")
    # os.startfile(filename, "print")
    file_path = input("Введіть шлях до файлу: ")
    try:
        import subprocess
        subprocess.run(['open', file_path], check=True)
    except:
        print("Помилка відкриття файлу.")


def get_data_dict():
    filename = input("Введіть ім'я файлу: ")
    key = int(input("Введіть ключ (число) для шифрування: "))
    alphabet = input("введіть тип алфавіту в форматі: EN або UA \n")
    cipher_type = input("Оберіть тип шифра: \n 1. Caesar \n 2. Tritemius \n")
    return {
        "fname": filename,
        "key": key,
        "alpha": alphabet,
        "ctype": cipher_type
    }


def encrypt_file():
    data = get_data_dict()
    if data["ctype"] == "1":
        cipher = CAESAR(data["key"], data["alpha"])
    else:
        cipher = TRITEMIUS(data["key"], data["alpha"])
    with open(data["fname"], 'r') as file:
        content = file.read()
        encrypted_content = cipher.enc(content)
    with open("encrypted_{}".format(data["fname"]), 'w') as file:
        file.write(encrypted_content)
        print("Файл зашифровано успішно!")


def decrypt_file():
    data = get_data_dict()
    if data["ctype"] == "1":
        cipher = CAESAR(data["key"], data["alpha"])
    else:
        cipher = TRITEMIUS(data["key"], data["alpha"])
    with open(data["fname"], 'r') as file:
        content = file.read()
        decrypted_content = cipher.dec(content)
    with open("decrypted_{}".format(data["fname"]), 'w') as file:
        file.write(decrypted_content)
        print("Файл розшифровано успішно!")


def show_developer_info():
    print("Розробник: Притула М.І. \n гр: 124м-22-1\n Версія програми: 1.0")


def exit_program():
    print("До побачення!")
    quit()


# MAIN CYCLE PROCESS
def main_menu():
    menu = """
        Меню: \n
        1. Створити файл \n
        2. Відкрити файл \n
        3. Зберегти файл \n
        4. Надрукувати файл \n
        5. Зашифрувати файл \n
        6. Розшифрувати файл \n
        7. Відомості про розробника \n
        8. Вийти з програми \n
    """

    while True:
        print(menu)
        
        choice = input("Введіть номер опції: ")

        if choice == "1":
            create_file()
        elif choice == "2":
            open_file()
        elif choice == "3":
            save_file()
        elif choice == "4":
            print_file()
        elif choice == "5":
            encrypt_file()
        elif choice == "6":
            decrypt_file()
        elif choice == "7":
            show_developer_info()
        elif choice == "8":
            exit_program()
        else:
            print("Неправильний вибір опції. Спробуйте ще раз.")


if __name__ == "__main__":
    main_menu()