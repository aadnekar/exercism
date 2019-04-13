import re
from collections import Counter

def word_count(phrase):
    return Counter(re.findall(r'\b[^\s,]+\b', re.sub(r'_',' ', phrase).lower()))