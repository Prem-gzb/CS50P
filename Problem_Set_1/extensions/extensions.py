# Prompting user to enter file name and converting everything to lowercase
file_type = input('Enter File Name: ').lower().strip()

if file_type.endswith('.gif'):
    print('image/gif')
elif file_type.endswith('.jpg'):
    print('image/jpeg')
elif file_type.endswith('.jpeg'):
    print('image/jpeg')
elif file_type.endswith('.png'):
    print('image/png')
elif file_type.endswith('.pdf'):
    print('application/pdf')
elif file_type.endswith('.txt'):
    print('text/plain')
elif file_type.endswith('.zip'):
    print('application/zip')
else:
    print('application/octet-stream')