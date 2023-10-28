def find_anagrams(word, candidates):
    returned = []
    for item in candidates:
        if word.lower() == item.lower():
            continue
        if sorted(word.lower()) == sorted(item.lower()):
            returned.append(item)
    return returned
        
