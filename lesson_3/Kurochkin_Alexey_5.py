
import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(number_jokes):
    """
    Функция возвращает 2 случайные шутки из списк

    :param number_jokes:
    :return:
    """
    result_jokes = []

    lists_list = nouns + adverbs + adjectives

    while len(result_jokes) != number_jokes:
        random.shuffle(lists_list)

        word_1 = random.choice(lists_list)
        word_2 = random.choice(lists_list)

        word = f'{word_1} {word_2}'

        result_jokes.append(word)

    return result_jokes


print(get_jokes(2))