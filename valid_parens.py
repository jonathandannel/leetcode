from helper import check

test = [
	"()",
	")(()))",
	"(",
	"(())((()())())"
]

def valid_paren(str):
	stack = []
	open_brack = "("
	closing_brack = ")"
	if len(str) % 2 != 0 or str[0] is not open_brack:
		return False
	for char in str:
		if char == open_brack:
			stack.append(char)
		if char == closing_brack and stack.pop() != open_brack:
			return False

	if stack == []:
		return True

check(valid_paren, test)