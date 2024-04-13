from seasons import *
import pytest

def main():
    test_check_birthdate()
    test_calculate_diff()

def test_check_birthdate():
    assert check_birthdate(2024,2,22) == date(2024,2,22)
    assert check_birthdate(22,2,2024) == 'Invalid Date'

# date of upload 11-April-2024. The difference need to be calculated accordingly
def test_calculate_diff():
    assert calculate_diff(date(2024,4,10)) == '1440'
    assert calculate_diff(date(1947,8,15)) == '40318560'


if __name__ == '__main__':
    main()