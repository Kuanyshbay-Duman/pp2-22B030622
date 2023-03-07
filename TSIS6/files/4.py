

example = "C:/Users/SULPAK/Documents/ПП2/Week6/TSIS5/12.txt"

with open(example, 'r') as e:
    lines = e.readlines()

num_lines = len(lines)
# for i in lines:
#     print(i)
print(f'The file has {num_lines} lines.')
