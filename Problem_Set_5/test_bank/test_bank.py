from bank import value
import pytest

def main():
    test_hello()
    test_not_start_with_hello()
    test_others()

def test_hello():
    assert value('hello') == 0
    assert value('hello, Prem') == 0

def test_not_start_with_hello():
    assert value('h....') == 20
    assert value('h...., Prem') == 20

def test_others():
    assert value('good Morning') == 100
    assert value('good morning, david') == 100

if __name__ == "__main__":
    main()