def is_bissextile(year):
    if are_divisible(year, 4) and are_divisible(year, 100) and are_divisible(year, 400):
        return True
    elif are_divisible(year, 4) and not are_divisible(year, 100):
        return True

    return False


def are_divisible(number, divider):
    return True if number % divider == 0 else False