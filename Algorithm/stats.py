#2. 给一组数，求mean，stdev，normalize，然后求L1norm。

nums = list(map(float, input().strip().split(', ')))
def stats(nums):
    if not nums:
        return 0
    mean = sum(nums)/len(nums)
    square_sum = 0
    L1_norm = 0
    for num in nums:
        square_sum += (num - mean)**2 
        L1_norm += abs(num)
    std = (square_sum/((len(nums))-1))**0.5
    return mean, std, L1_norm
print(stats(nums))
