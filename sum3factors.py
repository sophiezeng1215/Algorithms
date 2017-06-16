nums = list(map(int, input().strip().split(', ')))
def sum3factors(x):
    res = 0
    for num in nums:
        if num%3 == 0:
            res += int(num/3)
    return res
print (sum3factors(nums))
