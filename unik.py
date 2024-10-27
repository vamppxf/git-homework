def all_unique_chars(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

print(all_unique_chars("sup"))  
print(all_unique_chars("wrld"))  
