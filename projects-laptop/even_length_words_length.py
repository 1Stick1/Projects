def even_length_words_length(words):
    even_length = [len(word) for word in words if len(word) % 2 == 0]
    return even_length
words = ["apple", "banana", "cherry", "kiwi", "pear"]
print(even_length_words_length(words))