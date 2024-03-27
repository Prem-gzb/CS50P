while True:
    try:
        fract = input('Fraction: ')
        n = fract.find("/")
        num = fract[0:n]
        den = fract[n+1:]
        percent = round((int(num)/int(den)) * 100)

        if int(num) > int(den):
            continue

    except ZeroDivisionError:
        continue
    except ValueError:
        continue
    else:
        if percent >= 99:
                print('F')
        elif percent <= 1:
            print('E')
        else:
            print(f'{int(num)/int(den):.0%}')
        break