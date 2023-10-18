def is_armstrong_number(number):
    digits = list(str(number))
    arm = 0
    for dig in digits:
        arm = arm + (int(dig) ** len(digits))

    if arm == number:
        return True
    else:
        return False
    
             
    