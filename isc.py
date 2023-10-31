import os
def create_folder_if_not_exists(folder_name):
    try:
        os.makedirs(folder_name)
    except FileExistsError:
        pass
def main():
    folder_name = "user_data"  
    create_folder_if_not_exists(folder_name)
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    file_path = os.path.join(folder_name, "login.txt")

    try:
        with open(file_path, 'w') as file:
            file.write(f"Логин: {login}\nПароль: {password}")
        print(f"Логин и пароль записаны в {file_path}")
    except Exception as e:
        print(f"Произошла ошибка при записи данных: {e}")

if __name__ == "__main__":
    main()
