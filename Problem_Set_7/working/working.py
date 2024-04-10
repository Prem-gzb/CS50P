import re

def main():
    print(convert(input('Hours: ')))

def convert(s):
    time = re.search(r'^(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)$',s, re.IGNORECASE)

    if time:
        parts = time.groups()

        # Checking if hour is not more than 12. If yes, then raise ValueError
        if int(parts[0]) > 12 or int(parts[3]) > 12:
            raise ValueError

        # Checking if minute is given and it is not more than 59. If yes, then raise ValueError
        if (time.group(2) != None) or (time.group(5) != None):
            if (int(time.group(2)) > 59) or (int(time.group(5)) > 59):
                raise ValueError

        time_1 = convert_24_hour(parts[0],parts[1],parts[2])
        time_2 = convert_24_hour(parts[3],parts[4],parts[5])
        return time_1 +' to ' + time_2
    else:
        raise ValueError

def convert_24_hour(hh,mm,tt):
    if tt == 'PM':
        if int(hh) == 12:
            new_hour = hh
        else:
            new_hour = int(hh) + 12
    else:
        if int(hh) == 12:
            new_hour = 0
        else:
            new_hour = int(hh)

    new_time = (f"{new_hour:02}") + ':' + minute_check(mm)
    return new_time

def minute_check(minute):
    if minute == None:
        new_minute = 0
    else:
        new_minute = minute
    return f"{new_minute:02}"


if __name__ == '__main__':
    main()