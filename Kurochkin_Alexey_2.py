
text_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
numbers = ['+5']

text_string = ' '.join(text_list)
for s in text_string.split():
    if s.isdigit():
        numbers.append(int(s))

for num in numbers:
    index = text_list.index(str(num)) + 1
    text_list.insert(index, '"')
    if len(str(num)) == 1:
        text_list[index - 1] = '0{}'.format(num)
    elif num == '+5':
        text_list[index - 1] = '{}'.format('+05')
    text_list.insert(index - 1, '"')

print(text_list)
print(' '.join(text_list))



