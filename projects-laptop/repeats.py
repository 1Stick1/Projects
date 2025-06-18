def repeats(nums):
    repeat = {}
    for i in nums:
        repeat[i] = repeat.get(i, 0) + 1
    return repeat

nums = [1, 2, 2, 3, 4, 4, 4, 5]
print(repeats(nums))
