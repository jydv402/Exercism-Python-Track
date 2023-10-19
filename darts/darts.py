def score(x, y):
    rad_sq = x**2 + y**2

    if rad_sq <= 100:
        if rad_sq <= 25:
            if rad_sq <= 1:
                return 10
            return 5
        return 1
    return 0