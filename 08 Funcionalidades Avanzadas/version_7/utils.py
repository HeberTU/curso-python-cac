import re

def es_palindrome(s: str)->bool:
    s = s.lower().replace(" ", "")
    s = re.sub(r'[^\w\s]', '', s)
    return s == s[::-1]
