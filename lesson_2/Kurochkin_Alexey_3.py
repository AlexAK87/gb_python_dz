
distorted_data = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА',
                    'токарь высшего разряда нИКОЛАй', 'директор аэлита']

i = 0
for str_data in distorted_data:
    str_name = str_data.split()[-1]
    name = str_name.capitalize()

    print(f'Привет, {name}!')
    distorted_data[i] = str_data.replace(str_name, name)
    i += 1


print(distorted_data)


