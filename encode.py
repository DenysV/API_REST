import re 
def encode(text):
	pattern = re.compile("[A-Za-z]+")
	if pattern.fullmatch(text) is not None:
		res = ''
		k = 1
		text = text.upper()
		for i in range(1, len(text)):
			if text[i] == text[i-1]:
				k += 1
			else:
				res += text[i-1] + str(k)
				k = 1
		if res[-2] != text[-2]:
			res += text[-2] + str(k)
		return res
	else:
		return 'Word %s has spanish letters.' % text

print(encode('aáñÑabaccCBb'))
print(encode('aaaAabaccCBb'))
