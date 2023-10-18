def steps(number):
    step_count = 0
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number != 1:
            if number % 2 == 0:
                number = number // 2
            else:
                number = 3 * number + 1
            step_count += 1

    return step_count
