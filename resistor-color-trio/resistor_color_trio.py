def label(colors):
    clr_dict = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
    total = (clr_dict[colors[0]]*10 + clr_dict[colors[1]])*(10 ** clr_dict[colors[2]])
    
    
    if total < 10**9:
        if total < 10**6:
            if total < 10**3:
                return str(total) + " ohms"
            return str(total // 10**3) + " kiloohms"
        return str(total // 10**6) + " megaohms"
    return str(total // 10**9) + " gigaohms"

