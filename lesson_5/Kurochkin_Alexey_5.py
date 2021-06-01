import sys
import time

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

start_time = time.time()

print(src)
print(id(src))
print('memory before: {}'.format(sys.getsizeof(src)))

# 1 вариант
# for i in src:
#     if src.count(i) > 1:
#         src.remove(i)

# 2 вариант
for i in src:
    occurrences = src.count(i)
    if occurrences > 1:
        while occurrences != 0:
            src.remove(i)
            occurrences -= 1

print(src)
print(id(src))
print('memory after: {}'.format(sys.getsizeof(src)))

print("--- %s seconds ---" % (time.time() - start_time))
