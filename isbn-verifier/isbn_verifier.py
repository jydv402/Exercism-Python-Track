def is_valid(isbn):
    isbn_lst = list(isbn.replace('-',''))
    mult = 10
    total = 0

    if len(isbn_lst) != 10:
        return False

    if isbn_lst[-1] == 'X':
        isbn_lst[-1] = '10'

    for item in isbn_lst:
        if item not in ['0','1','2','3','4','5','6','7','8','9','10']:
            return False
        total += int(item)*mult
        mult -= 1

    return total % 11 == 0
    