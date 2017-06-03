def reverser():
    argument = 'Kung Olof'
    temp = []
    counter = 1
    while counter <= len(argument):
        temp.append(argument[-counter])
        counter += 1

    print(''.join(temp))

def check_prime(n):
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

def find_next_prime(number):
    prime_amount = 0
    x = 1
    while True:
        if checkPrime(number + x) is True:
            prime_amount += 1
        if prime_amount is 1:
            return number + x
        x += 1

def prime():
    y = 2
    while True:
        latest = find_next_prime(y)
        y = latest
        print(y)
        y += 1
        if y >= 60:
            break

prime()