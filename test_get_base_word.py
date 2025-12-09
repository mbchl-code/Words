import pytest
import random
from lab import get_base_word

words = ['КАНАТОХОДЕЦ', 'МАГНИТОФОН', 'БЛАГОПОЛУЧИЕ', 'ПРОДОЛЖИТЕЛЬНОСТЬ',
         'ВЗАИМОДЕЙСТВИЕ', 'ПРЕДСТАВИТЕЛЬ', 'ЧЕЛОВЕЧЕСТВО', 'УДОВЛЕТВОРЕНИЕ',
         'ЭЛЕКТРОПРОВОДНОСТЬ', 'КРИСТАЛЛИЗАЦИЯ', 'ДЕЗИНФЕКЦИЯ', 'КВАЛИФИКАЦИЯ',
         'ЛЕГИТИМНОСТЬ']

def test_get_base_word():
    result = False
    word = get_base_word()
    for i in range (0, len(words)):
        if word == words[i]:
            result = True
            break
    assert result == True