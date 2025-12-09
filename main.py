from core import inp_numb_of_players, game
from lab import get_base_word

def main():
    players = inp_numb_of_players()
    word = get_base_word()
    print("Исходное слово:", word)
    game(players)







if __name__ == '__main__':
    main()