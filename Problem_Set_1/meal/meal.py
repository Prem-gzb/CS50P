def main():
    t = input('What time it is: ')
    converted_time = convert(t)

    if converted_time >= 7 and converted_time <= 8:
        print('Breakfast Time')
    elif converted_time >= 12 and converted_time <= 13:
        print('Lunch Time')
    elif converted_time >= 18 and converted_time <= 19:
        print('Dinner Time')

def convert(t):
    h, m = t.split(':')
    h = float(h) + (float(m) / 60)
    return h

if __name__ == '__main__':
    main()