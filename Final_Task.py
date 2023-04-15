import os
import datetime

class InvalidDataException(Exception):
    pass

class InvalidFormatException(Exception):
    pass

class UserData:
    def __init__(self, surname, name, patronymic, birthdate, phone_number, gender):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthdate = birthdate
        self.phone_number = phone_number
        self.gender = gender

def parse_user_data(input_string):
    fields = input_string.split()

    if len(fields) != 6:
        raise InvalidDataException("Invalid number of fields")

    surname, name, patronymic, birthdate, phone_number, gender = fields

    # Validate birthdate
    try:
        birthdate = datetime.datetime.strptime(birthdate, '%d.%m.%Y').date()
    except ValueError:
        raise InvalidFormatException("Invalid birthdate format")

    # Validate phone number
    try:
        phone_number = int(phone_number)
    except ValueError:
        raise InvalidFormatException("Invalid phone number format")

    # Validate gender
    if gender not in ('m', 'f'):
        raise InvalidFormatException("Invalid gender format")

    return UserData(surname, name, patronymic, birthdate, phone_number, gender)

def write_user_data_to_file(user_data):
    filename = user_data.surname + ".txt"

    with open(filename, "a") as f:
        f.write(f"{user_data.surname} {user_data.name} {user_data.patronymic} {user_data.birthdate} {user_data.phone_number} {user_data.gender}\n")

if __name__ == "__main__":
    input_string = input("Введите данные пользователя: ")

    try:
        user_data = parse_user_data(input_string)
        write_user_data_to_file(user_data)
        print(f"Данные пользователя {user_data.surname} успешно записаны в файл")
    except InvalidDataException as e:
        print(f"Ошибка: {e}")
    except InvalidFormatException as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Ошибка: {type(e).__name__}: {e}")
