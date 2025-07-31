# Move all zeros to the end and sort non-zero elements 

nums = [0, -1, 0, 3, 5, 0, -2, 7] 
n = len(nums)

k = 0
for i in range(n):
    if nums[i] != 0:
        nums[k] = nums[i]
        k += 1 

for i in range(k-1):
    for j in range(k-i-1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

for i in range(k,n):
    nums[i] = 0

print(nums)