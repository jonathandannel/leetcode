# Given the array nums, for each nums[i]
# find out how many numbers in the array are smaller than it. 
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

def smaller_than_current(nums):
	length = len(nums)
	output = [0] * length
	for i in range(length):
		for j in range(length):
			if nums[j] < nums[i]:
				output[i] += 1
	return output