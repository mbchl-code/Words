from game.players import winners_checking
from game.words_checking import points_in_step, letter_repeat_error_message
from game.getting_base_word import get_base_word


def game(numb_players: str) -> None:
    word = get_base_word()
    used_words =[]
    point_count = [0 for _ in range(int(numb_players))]
    print(f"Исходное слово:                  {word}")
    print()
    print()
    counter_pass = 0
    while counter_pass != int(numb_players):

        for i in range(1, int(numb_players) + 1):
            print(f'Ход {i}-го игрока: ' , end="")
            word_curr = input().upper()

            if word_curr == '':
                e = "пропуск хода"
                counter_pass += 1
            else:
                counter_pass = 0
                if word_curr in used_words:
                    e = "ошибка - повтор"
                    point_count[i - 1] -= len(word_curr)
                else:
                    e = ""
                    used_words.append(word_curr)
                    curr_points = points_in_step(word_curr, word)
                    point_count[i-1] += points_in_step(word_curr, word)
                    if curr_points < 0:
                        e = letter_repeat_error_message(word_curr, word)
            print(f'Баллы {i}-го игрока = {point_count[i-1]} {e}')
            print()
            if counter_pass == int(numb_players):
                break
    winners_checking(point_count)



