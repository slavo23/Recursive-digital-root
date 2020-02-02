
def digit_sum(nums):
    return sum([int(digit) for digit in nums])


def digital_root_iterative(n):
    n_str = str(n)
    length = len(n_str)
    while length > 1:
        n_str = str(digit_sum(n_str))
        length -= 1
    return int(n_str)
