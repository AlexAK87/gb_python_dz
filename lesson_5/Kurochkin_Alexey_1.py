
def odd_nums(nums):
    """Генератор нечётных чисел"""

    for num in range(1, nums + 1, 2):
        yield num


number = 15

odd_to_15 = odd_nums(number)
print(type(odd_to_15))

try:
    while True:
        print(next(odd_to_15))
except StopIteration:
    print('...StopIteration...')
