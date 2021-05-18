import random

price_list = []
i = 0

for _ in range(20):
    lst = round(random.uniform(500, 10), 2)
    price_list.append(lst)

    i += 1

print(price_list)

for i in price_list:
    str_num = str(i)
    to_comma = str_num[:len(str_num) - 2]
    later_comma = str_num[len(str_num) - 2:]

    print(to_comma, later_comma)

