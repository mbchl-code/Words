from words_checking import points_in_step
from lab import get_base_word

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

#Переделать конец игры
def game(numb_players):
    word = get_base_word()
    used_words =[]
    point_count = [0,0,0,0]
    counter_pass = 0
    word_curr = ''
    print("Исходное слово:", word)
    while counter_pass < int(numb_players):
        counter_pass = 0
        for i in range(1, int(numb_players) + 1):
            print('Ход игрока: ', i)
            word_curr = input().upper()

            if word_curr == '':
                print('Игрок', i, 'пропустил ход')
                counter_pass += 1
            else:

                if(word_curr in used_words):
                    print('Это слово уже было')
                    point_count[i - 1] -= len(word_curr)
                else:
                    used_words.append(word_curr)
                    point_count[i-1] += points_in_step(word_curr, word)
                print('Количество очков игрока ', i,': ', point_count[i-1])
    print('Победил игрок', point_count.index((max(point_count)))+1, ' количество очков:', max(point_count))

