def get_float_input():
    while True:
        try:
            user_input = float(input("Введите дробное число: "))
            return user_input
        except ValueError:
            print("Вы ввели некорректное значение. Попробуйте еще раз.")

if __name__ == '__main__':
    result = get_float_input()
    print(f"Вы ввели число: {result}")
