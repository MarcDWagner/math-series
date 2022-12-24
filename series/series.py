
"""

"""

def fibonacci(n):
    if n < 0:
        print("Bad input, 0 or above")

    elif n == 0:
        return 0

    elif n == 1 or n ==2:
        return 1

    else:
        return fibonacci(n-1) + fibonacci(n-2)


def lucas(n):
    if n < 0:
        print("Bad input, 0 or above")

    elif n == 0:
        return 2

    elif n == 1:
        return 1

    else:
        return lucas(n-1) + lucas(n-2)


def sum_series(n, seq_0=0, seq_1=1):
    """
    returns nth element of either series, with fibonacci as default
    :param n:
    :param seq_0:
    :param seq_1:
    :return: fibonacci(n)
    """

    seq = [seq_0, seq_1]

    if n < 0:
        print("Bad input, 0 or above")

    elif n < 2:
        return seq[n]

    for i in range(n):
        next_number = seq[-1] + seq[-2]
        seq.append(next_number)

    else:
        return seq[n]


