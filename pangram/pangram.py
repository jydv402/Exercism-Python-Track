def is_pangram(sentence):
    alphs = set(chr(alph) for alph in range(97, 123))
    sent_set = set(sentence.lower())

    return sent_set.intersection(alphs) == alphs