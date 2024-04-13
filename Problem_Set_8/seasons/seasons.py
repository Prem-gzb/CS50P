from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        year, month, day = [int(x) for x in input('Date of Birth: ').split('-')]
    except ValueError:
        sys.exit('Invalid Date')

    dob = check_birthdate(year, month, day)
    diff_minutes = calculate_diff(dob)
    words = p.number_to_words(diff_minutes, andword='')
    print(words.capitalize() + ' minutes')

def check_birthdate(year, month, day):
    try:
        dob = date(year, month, day)
    except:
        return 'Invalid Date'
    return dob

def calculate_diff(dob):
    return str(((date.today() - dob).days) * 24 * 60)

if __name__ == '__main__':
    main()
