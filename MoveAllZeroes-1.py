# Move all zeros to the end while keeping the order of non-zero elements in-place.

nums = [-1, 0, 0, 3, 3, 3, 0, 0, 0]  
# nums = [0, -1, 0, 3, 5, 0, -2, 7] 

n = len(nums)
pos = 0

for i in range(n):
    if nums[i] != 0:
        nums[pos] = nums[i]
        pos += 1 
    
for i in range(pos, n):
    nums[i] = 0

print(nums)