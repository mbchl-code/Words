


def points_in_step(user_word: str, base_word: str) -> int:
    '''
    user_word: str: слово пользователя
    base_word: str: исходное слово
    Возвращает количество баллов за один ввод слова
    Если слово пользователя использовано повторно, функция вызываться не должна
    '''
    points = 0
    base_word = list(base_word)
    for letter in user_word:
        if letter not in base_word:
            points -= 1
        else:
            base_word.remove(letter)

    if points == 0:
        points = len(user_word)
    return points


