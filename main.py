from game.core import game
from game.players import inp_numb_of_players


def main():
    print()
    players = inp_numb_of_players()
    game(players)
    input()

if __name__ == '__main__':
    main()