import random

def main():
    level = get_level()
    random_num = random.randint(1, level)
    get_guess(random_num)

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level <= 0:
                continue
            return level
        except ValueError:
            continue
def get_guess(x):
    while True:
        try:
            guess = int(input('Guess: '))
            if guess <= 0:
                continue
            elif guess < x:
                print('Too small!')
                continue
            elif guess > x:
                print('Too large!')
                continue
            elif guess == x:
                print('Just right!')
                break
        except ValueError:
            continue
        return guess
    print(guess)

if __name__ == '__main__':
    main()