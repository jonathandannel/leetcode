# Given a non-negative integer num, return the number of steps to reduce it to zero. 
# If the current number is even, you have to divide it by 2,
# otherwise, you have to subtract 1 from it.

def numberOfSteps (num: int) -> int:
	if num == 0:
		return 0
	if num % 2 == 0:
		return 1 + numberOfSteps(num / 2)
	if num % 2 != 0:
		return 1 + numberOfSteps(num - 1)

def number_of_steps (num: int, steps: int = 0) -> int:
	if num == 0:
		return steps
	if num % 2 == 0:
		steps += 1
		return number_of_steps(num / 2, steps)
	if num % 2 != 0:
		steps += 1
		return number_of_steps(num - 1, steps)