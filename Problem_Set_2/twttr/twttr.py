def main():
    answer = input('Input: ')
    print(shorten(answer))


def shorten(word):
    vowels = ['a','e','i','o','u']

    for v in word:
        if v.lower() in vowels:
            word = word.replace(v, "")
    return word


if __name__ == '__main__':
    main()