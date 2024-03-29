def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    zero_index = s[2:].find('0')
    if 6 >= len(s) >= 2 and s[0:2].isalpha() and s.isalnum() and zero_index != 0:
        if s[2:4].isdigit() and s[-1].isalpha():
            return False
        else:
            return True
    else:
        return False

if __name__ == "__main__":
    main()