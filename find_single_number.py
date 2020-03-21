# Given a non-empty array of integers, every element appears twice except for one. Find that single one.
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

def find_single_number(nums: [int]) -> int:
	hash = {}
	for i in range(len(nums)):
		if nums[i] in hash:
			hash.pop(nums[i])
		else:
			hash[nums[i]] = 1
	for key in hash:
		return key

# Clever xor solution
def find_single(nums):
	seenonce = 0
	for x in range(len(nums)):
		seenonce = seenonce^nums[x]
	return seenonce	