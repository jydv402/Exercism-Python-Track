def resistor_label(colors):
    clr_dict = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}
    tol_dict = {"grey": " ±0.05%" , "violet": " ±0.1%" , "blue" : " ±0.25%" , "green" : " ±0.5%", "brown" : " ±1%" , "red" : " ±2%" , "gold": " ±5%", "silver" : " ±10%"}
    if len(colors) == 1:
        return str(clr_dict[colors[0]]) + " ohms"
    elif len(colors) == 4:
        total = (clr_dict[colors[0]]*10 + clr_dict[colors[1]])*(10 ** clr_dict[colors[2]])
    else:
        total = (clr_dict[colors[0]]*100 + clr_dict[colors[1]]*10 + clr_dict[colors[2]])*(10 ** clr_dict[colors[3]])
    total_str = ""
    
    
    if total < 10**9:
        if total < 10**6:
            if total < 10**3:
                total_str += str(total) + " ohms"
            else:
                total_str += str(total // 10**3) + " kiloohms" if total % 10**3 == 0 else str(total / 10**3) + " kiloohms"
        else:
            total_str += str(total // 10**6) + " megaohms" if total % 10**6 == 0 else str(total / 10**6) + " megaohms"
    else:
        total_str += str(total // 10**9) + " gigaohms" if total % 10**9 == 0 else str(total / 10**9) + " gigaohms"
      

    if len(colors) == 4:
        return total_str + tol_dict[colors[3]]
    else:
        return total_str + tol_dict[colors[4]]
