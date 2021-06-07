import re

valid_email = re.compile(r'^[^.!#$%@&+/=?^_`{|}~-][a-zA-Z0-9._-]+@[a-zA-Z0-9]+.[a-zA-Z0-9]{0,3}[^.!#$%&@+/=?^_`{|}~-]$')


def email_parse(email_address):
    assert valid_email.match(email_address), f'{email_address} не верный email'

    rezsult_dict = {}

    email_list = re.split(r'@', email_address)

    rezsult_dict.setdefault('username', email_list[0])
    rezsult_dict.setdefault('domain', email_list[1])

    return rezsult_dict


email_addres = input("Введеите email для проверки: ")

print(email_parse(email_addres))
