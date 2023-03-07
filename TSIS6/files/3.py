import os

example = "C:/Users/SULPAK/Documents/ПП2/Week6/TSIS5"

if os.path.exists(example):
    print('Path exists!!!')
    filename = os.path.basename(example)
    directory = os.path.dirname(example)
    print(f'Filename: {filename}')
    print(f'Directory: {directory}')
else:
    print('Path does not exist!!!')
