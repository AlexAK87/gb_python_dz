
number_input = input('Введите число от 0 до 10 на английском ')

number_translate = {'one': 'один', 'two': 'два', 'three ': 'три', 'four': 'четыре', 'five': 'пять',
                    'six ': 'шесть', 'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}

def num_translate(number):
    return number_translate.get(number)



print(num_translate(number_input))