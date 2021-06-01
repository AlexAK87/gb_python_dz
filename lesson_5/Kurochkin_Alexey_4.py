src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def output_nambers():
    result = []

    index_stop = 1
    for i in range(len(src)):
        if index_stop != len(src):
            if src[i] < src[i + 1]:
                result.append(src[i])
                result.append(src[i + 1])
        else:
            return result
        index_stop += 1


print(output_nambers())
