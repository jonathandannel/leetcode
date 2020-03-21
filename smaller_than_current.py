# Given the array nums, for each nums[i]
# find out how many numbers in the array are smaller than it. 
# Input: nums = [8,1,2,2,3]
# Output: [4,0,1,1,3]

def smaller_than_current(nums):
	output = [0] * len(nums)
	for i in range(len(nums)):
		for j in range(len(nums)):
			if nums[j] < nums[i]:
				output[i] += 1
	return output

def smaller_than_c(nums):
	hash = {}
	for i in range(len(nums)):
		hash[i] = 0
		for j in range(len(nums)):
			if nums[j] < nums[i]:
				hash[i] += 1
	return hash.values()

def smaller_than_curr(nums):
	result = [0] * len(nums)
	hash = {}
	for i in range(len(nums)):
		if nums[i] in hash:
			result[i] = hash[nums[i]]
			continue
		for j in range(len(nums)):
			if i != j:
				if nums[i] > nums[j]:
					result[i] += 1
		hash[nums[i]] = result[i]
	return result
