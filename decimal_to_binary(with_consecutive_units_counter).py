def decimal_to_binary(n: int) -> tuple:
    """ Function to convert decimal number to binary number.

        Additional task: count maximum number of consecutive units in binary number.
    """
    binary_string = ''
    max_sequence = 0
    counter = 0
    while n > 0:
        if n % 2 == 1:
            counter += 1
        elif n % 2 == 0:
            if counter >= max_sequence:
                max_sequence = counter
                counter = 0
            else:
                counter = 0
        binary_string += str(n % 2)
        n //= 2
    return binary_string[::-1], max_sequence if max_sequence > counter else counter


if __name__ == '__main__':
    n = int(input())
    # solution using self-made function:
    print(decimal_to_binary(n)[1])
    # built-in solution:
    print(max(len(x) for x in (bin(n)[2:].split('0'))))
