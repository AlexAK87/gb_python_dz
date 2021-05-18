import random

price_list = []

for _ in range(20):
    lst = round(random.uniform(500, 10), 2)
    price_list.append(lst)

#* Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп (например «5 руб 04 коп»).
# Подумать, как из цены получить рубли и копейки, как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп)
print('*' * 25 + ' 1')
print(price_list)

result_text = ""

for i in price_list:
    str_num = str(i)
    to_comma = str_num[:str_num.find('.')]
    later_comma = str_num[str_num.find('.') + 1:]

    if len(later_comma) == 1:
        later_comma = '0' + later_comma

    if result_text != "":
        result_text = result_text + f', {to_comma} руб. {later_comma} коп.'
    else:
        result_text = f'{to_comma} руб. {later_comma} коп.'

print(result_text)

#* Вывести цены, отсортированные по возрастанию, новый список не создавать (доказать, что объект списка после сортировки остался тот же).
print('*' * 25 + ' 2')
print(id(price_list))
price_list.sort()
print(price_list)
print(id(price_list))

# * Создать новый список, содержащий те же цены, но отсортированные по убыванию.
print('*' * 25 + ' 3')

price_list_copy = price_list.copy()
price_list_copy.reverse()
print(price_list_copy)

#* Вывести цены пяти самых дорогих товаров. Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
print('*' * 25 + ' 4')
print(sorted(price_list_copy[:5]))