
def thesaurus(*args):
    """
    Функция возвращает словарь, в котором ключи — первые буквы имен,
    а значения — списки, содержащие имена и фамилию, начинающиеся с соответствующей буквы
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

    return result_dict

def thesaurus_adv(*args):
    result_dict = {}

    for name in args:
        first_letter_last_name = name.split()[1][0]

        array_list = result_dict.get(first_letter_last_name)

        if array_list == None:
            result_dict.setdefault(first_letter_last_name, thesaurus(name))
        else:
            key1 = ''.join(array_list.keys())
            key2 = ''.join(thesaurus(name).keys())
            if key1 == key2:
                array_list1 = result_dict.get(first_letter_last_name).get(key1)
                array_list1.append(name)
            else:
                result_dict.get(first_letter_last_name).setdefault(key2, [name])


    return result_dict

print(thesaurus_adv("Иван Сергеев", "Инна Серова",  "Петр Алексеев", "Илья Иванов", "Анна Савельева"))