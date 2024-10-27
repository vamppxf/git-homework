def char_count(s):
    datvla = {}
    for char in s:
        datvla[char] = datvla.get(char, 0) + 1
    return datvla

print(char_count("zdarova"))
