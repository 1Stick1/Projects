def double_even_numbers(nums):
    even_numbers = [num*2 for num in nums if num % 2 == 0]
    return even_numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(double_even_numbers(nums))