tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Борис', 'Елена']

klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

if len(klasses) < len(tutors):
    klasses.append(None)

tem = ([tutor, klasse] for tutor, klasse in zip(tutors, klasses))
print(type(tem))


try:
    while True:
        print(tuple(next(tem)))
except StopIteration:
    print('...StopIteration...')
