input = [8,1,2,2,3]

def smallerNumbersThanCurrent(nums):
	count = {}        
	for i, n in enumerate(sorted(nums)):
		if n not in count:
			count[n] = i
	return [count[n] for n in nums]

print(smallerNumbersThanCurrent(input))