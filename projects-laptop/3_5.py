def filter(numbers):
    filtered = [num for num in numbers if num % 3 == 0 and num % 5 == 0]
    return filtered
numbers = [15, 30, 22, 45, 50, 18, 75]
print(filter(numbers))