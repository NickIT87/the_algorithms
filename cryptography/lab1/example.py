import os

def create_file():
    filename = input("Введіть ім'я файлу: ")
    with open(filename, 'w') as file:
        print("Файл створено успішно!")

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
    filename = input("Введіть ім'я файлу: ")
    os.startfile(filename, "print")

def encrypt_file():
    filename = input("Введіть ім'я файлу: ")
    key = input("Введіть ключ для шифрування: ")
    with open(filename, 'r') as file:
        content = file.read()
        # реалізуйте процес шифрування тут
        encrypted_content = content[::-1] # це тільки приклад, не використовуйте його для справжніх шифрування!
    with open(f"encrypted_{filename}", 'w') as file:
        file.write(encrypted_content)
        print("Файл зашифровано успішно!")

def decrypt_file():
    filename = input("Введіть ім'я файлу: ")
    key = input("Введіть ключ для розшифрування: ")
    with open(filename, 'r') as file:
        content = file.read()
        # реалізуйте процес розшифрування тут
        decrypted_content = content[::-1] # це тільки приклад, не використовуйте його для справжніх шифрування!
    with open(f"decrypted_{filename}", 'w') as file:
        file.write(decrypted_content)
        print("Файл розшифровано успішно!")

def show_developer_info():
    print("Розробник: Ваше ім'я та прізвище\nEmail: ваш email\nВерсія програми: 1.0")

def exit_program():
    print("До побачення!")
    quit()

while True:
    print("Меню:")
    print("1. Створити файл")
    print("2. Відкрити файл")
    print("3. Зберегти файл")
    print("4. Надрукувати файл")
    print("5. Зашифрувати файл")
    print("6. Розшифрувати файл")
    print
    print("7. Відомості про розробника")
    print("8. Вийти з програми")

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
