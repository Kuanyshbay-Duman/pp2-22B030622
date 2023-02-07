def reverse_sentence(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)


sentence = input("Enter a sentence: ")
reversed_sentence = reverse_sentence(sentence)
print("Reversed sentence:", reversed_sentence)
