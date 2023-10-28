def commands(binary_str):
    code_dict = {0: "wink", 1: "double blink", 2: "close your eyes", 3: "jump"}
    handshake = []
    length = 5
    dict_index = 0

    while(length > 1):
        if binary_str[length-1] == "1":
            handshake.append(code_dict[dict_index])
        length -= 1
        dict_index += 1

    if binary_str[0] == "1":
        handshake.reverse()

    return handshake