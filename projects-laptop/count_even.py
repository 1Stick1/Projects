def count(numbers):
    count = {
        "even": sum([1 for num in numbers if num % 2 == 0]),
        "not even": sum([1 for num in numbers if num % 2 == 1])
    }
    return count
numbers = [10, 23, 45, 66, 78, 99, 100, 33]
print(count(numbers))