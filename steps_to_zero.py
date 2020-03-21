def numberOfSteps (num: int) -> int:
	if num == 0:
		return 0

	if num % 2 == 0:
		return 1 + numberOfSteps(num / 2)

	if num % 2 != 0:
		return 1 + numberOfSteps(num - 1)

print(numberOfSteps(14))