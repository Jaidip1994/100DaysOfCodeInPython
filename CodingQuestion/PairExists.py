nums = [8, 7, 2, 5, 3, 1]
target = 4

# Using sorting mechanism
def usingSortingMechanism(nums):
    nums.sort()
    low, high = 0, len(nums) - 1
    while low < high:
        if nums[low] + nums[high] == target:
            return (f'Pairs are {nums[low]} , {nums[high]}')
        elif nums[low] + nums[high] < target:
            low += 1
        else:
            high -= 1
    return (f'No Pairs Exist')

print(usingSortingMechanism(nums))

# Using Hashing Mechanism
def hashAlgo(nums):
    elem_dict= dict.fromkeys(nums)
    for elem in elem_dict:
        if target - elem in elem_dict:
            return (f'Pairs are {target-elem} , {elem}')
    return (f'No Pairs Exist')

print(hashAlgo(nums))