example = "C:/Users/SULPAK/Documents/ПП2/Week6/TSIS5/12.txt"
my_opinion = ['PP2', 'is', 'strange', 'for', 'me']

with open(example, 'w') as e:

    for i in my_opinion:
        e.write(f'{i}\n')

t = open(example, 'r')
print(t.read())
