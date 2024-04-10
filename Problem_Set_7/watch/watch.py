import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    match = re.search(r'.+src="http(s)?:\/\/(?:www.)?youtube\.com\/embed\/(.+?)"', s)
    if match:
        link = 'https://youtu.be/' + match.group(2)
        return link
    else:
        return None

if __name__ == "__main__":
    main()