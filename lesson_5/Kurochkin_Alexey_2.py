
def odd_nums(nums):
    """Генератор нечётных чисел"""

    nums_gen = (num for num in range(nums + 1) if num % 2 != 0)

    return nums_gen


number = 15

odd_to_15 = odd_nums(number)
print(type(odd_to_15))

try:
    while True:
        print(next(odd_to_15))
except StopIteration:
    print('...StopIteration...')
