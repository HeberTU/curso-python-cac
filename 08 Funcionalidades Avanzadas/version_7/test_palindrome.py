import pytest
from utils import es_palindrome

@pytest.mark.parametrize("palindrome", [
    "",
    "a",
    "Bob",
    "anita lava la tina",
    "anita lava la tina?",
])
def test_es_palindrome(palindrome):
    assert es_palindrome(palindrome)

@pytest.mark.parametrize("no_palindrome", [
    "abc",
    "abab",
])
def test_no_es_palindrome(no_palindrome):
    assert not es_palindrome(no_palindrome)