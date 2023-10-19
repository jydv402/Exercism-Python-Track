def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    iterate = number // 2 + 1
    sum = 0
    for value in range(1 , iterate):
        if number % value == 0:
            sum += value

    if sum < number:
        return "deficient"
    elif sum > number:
        return "abundant"
    return "perfect"
        
    