def inp_numb_of_players():
    while True:
        numb_players = input("Введите число от 2 до 4: ")
        if (numb_players.isdigit()) and (4 >= int(numb_players) >= 2):
            number = int(numb_players)
            print(f"Количество игроков: {number}")
            break
        else:
            if not (numb_players.isdigit()):
                print("Ошибка: Ввод содержит не цифры")
            else:
                print("Ошибка: Число игроков должно быть от 2-х до 4-х")


    return numb_players

def game(numb_players):
    counter_pass = 0
    word_curr = ''
    while counter_pass < int(numb_players):
        counter_pass = 0
        for i in range(1, int(numb_players) + 1):
            word_curr = input()
            if word_curr == '':
                print('Игрок', i, 'пропустил ход')
                counter_pass += 1
            elif ...:


