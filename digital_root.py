
def digital_root(n):
    n_str = str(n)
    digits = sum([int(digit) for digit in n_str])
    if len(n_str) > 1:
        return digital_root(digits)
    return digits
