from typing import List


def winners_checking(point_count: List[int]) -> None:
    max_points = max(point_count)
    winners = []

    for i, score in enumerate(point_count):
        if score == max_points:
            winners.append(i + 1)

    if len(winners) == 1:
        print(f'ИГРА ОКОНЧЕНА, ПОБЕДИЛ {point_count.index((max(point_count))) + 1}-й ИГРОК')
    else:
        print(f'ИГРА ОКОНЧЕНА, ПОБЕДИЛИ', end=" ")
        for i in winners[:-1]:
            print(i, end="-й, ")
        print(f'{winners[-1]}-й ИГРОКИ')


def inp_numb_of_players():
    while True:
        numb_players = input("Введите число от 2 до 4:         ")
        print()
        if (numb_players.isdigit()) and (4 >= int(numb_players) >= 2):
            number = int(numb_players)
            print(f"Число игроков:                   {number}")
            print()
            break
        else:
            if not numb_players.isdigit():
                print("Ошибка: Ввод содержит не цифры")
            else:
                print("Ошибка: Число игроков должно быть от 2-х до 4-х")

    return numb_players