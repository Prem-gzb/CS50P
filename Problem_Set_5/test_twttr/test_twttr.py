import pytest
from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten('Twitter') == 'Twttr'
    assert shorten('CS50P') == 'CS50P'
    assert shorten('OrAnge') == 'rng'
    assert shorten('123') == '123'
    assert shorten('This is CS50P') == 'Ths s CS50P'
    assert shorten('Good Day !') == 'Gd Dy !'

if __name__ == "__main__":
    main()