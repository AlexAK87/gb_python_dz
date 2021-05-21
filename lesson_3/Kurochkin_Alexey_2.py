
number_input = input('Введите число от 0 до 10 на английском языке, первая буква в верхнем или нижнем регистре: ')

number_translate = {'one': 'один', 'two': 'два', 'three ': 'три', 'four': 'четыре', 'five': 'пять',
                    'six ': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate_adv(number):
    if number.istitle():
        result_number = number_translate.get(number.lower())
        return result_number.capitalize()
    else:
        return number_translate.get(number)


print(num_translate_adv(number_input))
