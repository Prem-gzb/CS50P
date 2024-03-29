def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(gauge(percentage))

def convert(fraction):
    while True:
        try:
            index = fraction.find("/")
            num = int(fraction[:index])
            den = int(fraction[index+ 1:])

            if (num/den) <= 1:
                percentage = round((num / den) * 100)
                return percentage
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return (str(percentage) + "%")

if __name__ == "__main__":
    main()