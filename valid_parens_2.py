from helper import check

test = [
	"({}<>)",
	")(()))",
	"<{()}()>",
	"<{()}((()<()>)())>"
]

def valid_paren(str):
	stack = []
	
	bracks = {
		")": "(",
		"}": "{",
		">": "<"
	}

	if len(str) % 2 != 0 or str[0] in bracks:
		return False

	for char in str:
		if char in bracks:
			if stack.pop() != bracks[char]:
				return False
		else:
			stack.append(char)

	if stack == []:
		return True

check(valid_paren, test)