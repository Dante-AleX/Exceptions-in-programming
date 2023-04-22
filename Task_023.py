while True:
    user_input = input("Введите что-нибудь: ")
    if not user_input:
        raise Exception("Вы ввели пустую строку, попробуйте еще раз")
    else:
        print("Вы ввели: ", user_input)
