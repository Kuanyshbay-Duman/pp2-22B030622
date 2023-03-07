import os

example = "C:/Users/SULPAK/Documents/ПП2/Week7/TSIS6/files/delete.txt"


if os.path.exists(example):
    if os.access(example, os.W_OK):
        os.remove(example)
        print(f"{example} deleted successfully.")
    else:
        print(f"You don't have access to delete {example}.")
else:
    print(f"{example} does not exist!")
