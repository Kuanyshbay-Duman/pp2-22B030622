def counting_certain_letters(str):
    cnt1 = 0
    cnt2 = 0
    for i in str:
        if i.isupper():
            cnt1 = cnt1 + 1
        elif i.islower():
            cnt2 += 1
    return cnt1, cnt2


word = input("Enter a word: ")
print("The number of uppercase and lowercase letters are: ")
print(counting_certain_letters(word))
