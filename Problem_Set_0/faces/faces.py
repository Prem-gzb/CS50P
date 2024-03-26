def main():
    msg = input('How are you feeling today: ')
    print(convert(msg))

def convert(msg):
    # replacing with happy emoji
    msg_1 = msg.replace(":)",'🙂')

    # replacing with sad emoji in msg_1
    msg_2 = msg_1.replace(":(",'🙁')

    return msg_2

main()