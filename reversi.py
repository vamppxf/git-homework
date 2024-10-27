def reverse_string(s):
    reversi = ""
    for char in s:
        reversi = char + reversi
    return reversi

print(reverse_string("avoradz"))
