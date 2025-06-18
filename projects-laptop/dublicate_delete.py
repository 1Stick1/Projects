def duplicate_delete(numbers):
    deleted = sorted(set(numbers))
    return deleted
numbers = [5, 3, 8, 3, 1, 5, 7, 8, 2, 2]
print(duplicate_delete(numbers))