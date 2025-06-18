def change(words):
    changed = ['...' if len(word) > 4 else word for word in words ]
    return changed
words = ["кот", "собака", "дом", "автомобиль", "море"]
print(change(words))