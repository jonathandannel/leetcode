# Print the result of a function on a list
def check(fn, input):
	for item in input:
		res = fn(item)
		print(res)
