import random

def main():
    score = 0
    no_of_tries = 0
    i = 0
    level = get_level()

    while i < 10:
        try:
            if no_of_tries == 0:
                x, y = generate_integer(level)
            ans = int(input(f'{x} + {y} = '))
        except ValueError:
            print('EEE')
            no_of_tries += 1
        else:
            if ans== (x+ y):
                score += 1
                no_of_tries = 0
                i += 1
            else:
                print('EEE')
                no_of_tries += 1
        if no_of_tries == 3:
            i += 1
            print(f'{x} + {y} = {x + y}')
            no_of_tries = 0
    print('Score: ', score)

def generate_integer(level):
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x, y

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level in [1,2,3]:
                return level
            else:
                continue
        except ValueError:
            continue

if __name__ == '__main__':
    main()