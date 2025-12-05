import pytest
from re import findall

def test_findall_basic():
    text = "apple banana apple orange banana apple"
    pattern = r"apple"
    result = findall(pattern, text)
    assert result == ["apple", "apple", "apple"]

def test_findall_digits():
    text = "There are 24 hours in 1 day and 365 days in 1 year."
    pattern = r"\d+"
    result = findall(pattern, text)
    assert result == ["24", "1", "365", "1"]

def test_findall_words_starting_with_b():
    text = "ball bat cat bag dog bone"
    pattern = r"\bb\w+"
    result = findall(pattern, text)
    assert result == ["ball", "bat", "bag", "bone"]

def test_findall_no_matches():
    text = "hello world"
    pattern = r"\d+"
    result = findall(pattern, text)
    assert result == []
