from plates import is_valid
import pytest

def main():
    test_length()
    test_first_two()
    test_space_punctuation()
    test_num_not_in_middle()

def test_length():
    assert is_valid('HELLO') == True
    assert is_valid('G') == False
    assert is_valid('GOODBYE') == False

def test_first_two():
    assert is_valid('HE') == True
    assert is_valid('05') == False
    assert is_valid('P1') == False

def test_space_punctuation():
    assert is_valid('HI, CS') == False
    assert is_valid('PI3.14') == False

def test_num_not_in_middle():
    assert is_valid('CS50P') == False
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False

if __name__ == "__main__":
    main()
