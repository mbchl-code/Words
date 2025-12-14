


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


def letter_repeat_error_message(user_word: str, base_word: str) -> str:
    base_word = list(base_word)
    for i in range(len(user_word)):
        if user_word[i] not in base_word:
            user_word = user_word[:i] + user_word[i].lower() + user_word[i+1:]
        else:
            base_word.remove(user_word[i])


    return 'ошибка: ' + user_word



