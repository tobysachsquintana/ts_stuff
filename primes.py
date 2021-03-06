"""
A script that determines whether or not a number is prime. To run this script,
navigate to the directory that stores this script and type:
python primes.py
"""


def is_prime(n):
    """
    Determines whether a number is prime.
    :param n: A positive integer.
    :return: A message stating whether or not the number is prime.
    """
    true_msg = str(n) + ' is prime'
    false_msg = str(n) + ' is not prime'
    if n == 2:
        return true_msg
    if n == 3:
        return true_msg
    if n % 2 == 0:
        return false_msg
    if n % 3 == 0:
        return false_msg

    k = 5
    x = 2

    while k * k <= n:
        if n % k == 0:
            return false_msg

        k += x
        x = 6 - x
    return true_msg

if __name__ == '__main__':
    number_in = raw_input('Please enter a positive integer: ')
try:
    number_in = int(number_in)
    print(is_prime(number_in))
except ValueError:
    print('Enter an integer and try again')
