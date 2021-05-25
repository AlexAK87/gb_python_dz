
def thesaurus(*args):
    """
    Функция возвращает словарь, в котором ключи — первые буквы имен,
    а значения — списки, содержащие имена, начинающиеся с соответствующей буквы
    :param args:
    :return:
    """
    result_dict = {}

    for name in args:
        first_letter = name[0]
        array_list = result_dict.get(first_letter)
        if array_list == None:
            result_dict.setdefault(first_letter, [name])
        else:
            array_list.append(name)

    # Сортировка результата по ключу
    list_key = list(result_dict.keys())
    list_key.sort()

    result_dict_copy = result_dict.copy()
    result_dict.clear()

    for key in list_key:
        result_dict.setdefault(key, result_dict_copy.get(key))

    return result_dict

print(thesaurus("Иван", "Мария", "Петр", "Илья", 'Алексей'))

