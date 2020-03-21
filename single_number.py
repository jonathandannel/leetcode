def find_single_number(nums):
	hash = {}
	for i in range(len(nums)):
		if nums[i] not in hash:
			hash[nums[i]] = 1
		elif nums[i] in hash:
			hash[nums[i]] = hash[nums[i]] + 1
	for attr in hash:
		if hash[attr] == 1:
			return attr
print(find_single_number([1, 1, 2, 2, 3, 3, 4, 5, 5]))

# Clever xor solution
def find_single(nums):
	seenonce = 0
	for x in range(len(nums)):
		seenonce = seenonce^nums[x]
	return seenonce

print(find_single([1, 1, 2, 2, 4, 5, 5]))