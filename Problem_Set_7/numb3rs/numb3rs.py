import re
import sys

def main():
    print(validate(input('IPv4 Address:')))

def validate(ip):
    parts = ip.split('.')
    if re.search(r'^(\d+)\.(\d+)\.(\d+)\.(\d+)$', ip):
        for part in parts:
            if int(part) < 0 or int(part) > 255:
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    main()