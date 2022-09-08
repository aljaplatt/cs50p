filename = input("File name: ").strip().lower()

# check for dot .
if '.' in filename:
    # print('has extension')
    if filename[-3:] == 'pdf' or filename[-3:] == 'zip':
        print(f"application/{filename[-3:]}")
    elif filename[-3:] == 'gif' or filename[-3:] == 'png':
        print(f"image/{filename[-3:]}")
    elif filename[-4:] == 'jpeg' or filename[-3:] == 'jpg':
        print(f"image/jpeg")
    elif filename[-3:] == 'txt':
        print(f"text/plain")
    elif filename[-3:] == 'bin':
        print(f"application/octet-stream")
else:
    print('application/octet-stream')