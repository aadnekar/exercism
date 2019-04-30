import re

def is_isogram(string):
    x = re.findall(r'[a-z]', string.lower())
    if len(x) != len(set(x)):
        return False
    return True
