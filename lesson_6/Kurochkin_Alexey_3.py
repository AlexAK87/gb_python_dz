import sys
import json


def read_files(dir_file, users=True):
    with open(dir_file, 'r', encoding='utf-8') as file_read:
        result_list = []
        for line in file_read:
            if users:
                result_list.append(line.replace(',', ' ').strip())
            else:
                in_hobby = line.find(',', 0, len(line))
                if in_hobby > 0:
                    hobby_list = []
                    start_hobby = 0
                    hobby = 0
                    while True:
                        start_hobby = line.find(',', start_hobby, len(line))
                        if start_hobby == -1:
                            line_hobby = line[hobby + 1:]
                            hobby_list.append(line_hobby.strip())
                            break
                        else:
                            line_hobby = line[hobby:start_hobby]
                            hobby_list.append(line_hobby.replace(',', ''))
                            hobby = start_hobby
                            start_hobby += 1

                    result_list.append(hobby_list)
                else:
                    result_list.append(line)

    return result_list


def read_write_files():
    users = read_files('users.csv')
    hobby = read_files('hobby.csv', False)

    result_dict = {}
    i = 0

    for user in users:
        if len(users) > len(hobby):
            if i != len(hobby):
                result_dict.setdefault(user, hobby[i])
            else:
                result_dict.setdefault(user, None)

            i += 1
        else:
            sys.exit(1)

    with open('users_task_3.txt', 'w', encoding='utf-8') as files:
        json.dump(result_dict, files, sort_keys=True, indent=4)

    with open('users_task_3.txt', 'r', encoding='utf-8') as files:
        return json.load(files)


if __name__ == '__main__':
    print(read_write_files())
