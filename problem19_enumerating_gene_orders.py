def permutations(nums):
    if len(nums) == 1:
        return [nums]
    
    result = []
    for i in range(len(nums)):
        current = nums[i]
        remaining = nums[:i] + nums[i+1:] 
        
        for perm in permutations(remaining):  
            result.append([current] + perm)
    
    return result

n = 5
nums = list(range(1, n + 1))

total = 1
for i in range(1, n + 1):
    total *= i

all_perms = permutations(nums)

print(total)
for perm in all_perms:
    print(" ".join(str(x) for x in perm))