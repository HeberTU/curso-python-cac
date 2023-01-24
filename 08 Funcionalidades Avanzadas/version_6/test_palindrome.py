from utils import es_palindrome

def test_es_palindrome_string_vacia():
    assert es_palindrome("")

def test_es_palindrome_caracter():
    assert es_palindrome("a")

def test_es_palindrome_mayusculas_minusculas():
    assert es_palindrome("Bob")

def test_es_palindrome_con_espacios():
    assert es_palindrome("anita lava la tina")

def test_es_palindrome_con_signos():
    assert es_palindrome("anita lava la tina?")

def test_no_es_palindrome():
    assert not es_palindrome("abc")

def test_no_es_palindrome_por_poco():
    assert not es_palindrome("abab")