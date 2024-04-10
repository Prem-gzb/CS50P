from um import count

def main():
    test_for_case()
    test_word_having_um()
    test_for_white_space()

def test_for_case():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2

def test_word_having_um():
    assert count('yummy') == 0
    assert count('Mumbai') == 0

def test_for_white_space():
    assert count('Hello, um world') == 1
    assert count('Um?') == 1

if __name__ == "__main__":
    main()