def is_isogram(string):
    string_list = list(string.lower())
    ltr_list = []
    decider = True

    for letter in string_list:
        if letter != ' ' and letter != '-':
            if ord(letter) in ltr_list:
                decider = False
            ltr_list.append(ord(letter))
            
    return decider