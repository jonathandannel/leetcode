def atoi(s):
	output = ""
	negative = False
	for x in s:
		if x is "-" and len(output) == 0:
			negative = True
		if x.isdigit():
			output += x
	num = int(output)
	if negative:
		return 0 - num
	else: 
		return num

print(atoi("  5555-3ss41 "))