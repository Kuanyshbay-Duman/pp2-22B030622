with open('example.txt', 'r') as source:
    with open('new_file.txt', 'w') as new:
        new.write(source.read())
