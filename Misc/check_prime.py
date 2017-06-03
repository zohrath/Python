def inspect_number(n) -> bool:
    """
    Checks if an input is a prime number
    :param n: The number to check
    :return: Bool
    """
    number_of_divisible_numbers = 0
    comparison_number = 1
    while comparison_number <= n:
        if n % comparison_number is 0:
            number_of_divisible_numbers += 1
        if number_of_divisible_numbers > 2:
            return False
        if comparison_number >= n:
            return True
        comparison_number += 1

def find_next_prime(number) -> int:
    """
    Finds the next prime after number argument
    :rtype: Int
    """
    prime_amount = 0
    x = 1
    while True:
        if inspect_number(number + x) is True:
            prime_amount += 1
        if prime_amount is 1:
            return number + x
        x += 1

def check():
    """
    Method to check a range of values y and print all prime numbers contained in the range
    """
    y = 2
    while True:
        latest = find_next_prime(y)
        y = latest
        print(y)
        y += 1
        if y >= 60:
            break
