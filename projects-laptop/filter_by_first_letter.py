def filter_by_letter(words, letter):
    result = [num for num in words if num[0] == letter]
    return result
words = ["арбуз", "апельсин", "банан", "авокадо", "груша"]
letter = "а"
print(filter_by_letter(words, letter))