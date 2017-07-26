# minimal parsing


def get_matched_lines(content, expr):
	lines = []
	content = str_to_list(content)
	for line in content:
		if expr in line:
			lines.append(line)
	return lines


def check_type(content):
	if type(content) == type(""):
		return 'str'
	return None


def str_to_list(content, separator='\\n'):
	if check_type(content) ==  'str':
		if separator in content:
			content = content.split(separator)
			return content
	return None


def minimize_white_space(line):
	characters = []
	keep = True
	for c in line:
		if not keep and ord(c) != 32:
			keep = True
		if keep:
			characters.append(c)
			if ord(c) == 32:
				keep = False
	return ''.join(characters)


def split_by_free_space(line):
	line = minimize_white_space(line)
	line = line.split(' ')
	return line


def get_first_word(text):
	return text.split(' ')[0]


def get_nth_word(text, n):
	'''
		Returns a word from a one-line sentence with n starting at 1 (not 0).

		Example:
			
			"This is a sentence."

			n  =  1: "This"
			n  =  2: "is"
			...
			n  >  4: "<NULL_INDEX>"
			
			Reverse Index:
			n  = -1: "sentence."
			n  = -2: "a"
			...
			n  < -4: "<NULL_INDEX>"

			Zero is not a number:
			n  =  0: "<NULL_INDEX>"

		Args:
			text (str): a one-line sentence is expected
			n (int): index of word, starting at 1 (not 0)

		Returns:
			str: the word at index n with no spaces
	'''
	wordList = split_by_free_space(text)
	length = len(wordList)
	if n == 0 or n > length or n < length*(-1):
		return '<NULL_INDEX>'
	else:
		if n > 0:
			n = n - 1
		# otherwise, n < 0 and it need not be modified
		return split_by_free_space(text)[n]


def isLetter(c):
	c = ord(c)
	if c >= 65 and c <= 90:
		return True
	if c >= 90 and c <= 122:
		return True
	return False


def isDigit(c):
	c = ord(c)
	if c >= 48 and c <= 57:
		return True


def isAcceptedCharacter(c, accepted=[]):
	if len(accepted) > 0:
		c = ord(c)
		for character in accepted:
			if c == ord(character):
				return True
	return False


def validate_input(input):
	if not type(input) == type(''):
		return None
	# first char cannot be a number
	if input and not isLetter(input[0]):
		return None
	for c in input[1:]:
		c = ord(c)
		# space, 0
		if c != 45 and c < 48:
			return None
		# 9, A
		if c > 57 and c < 65:
			return None
		# Z, a, -
		if c > 90 and c < 97 and c != 95:
			return None
		# z
		if c > 122:
			return None
	return input


def remove_list_item_by_element(item, items):
	try: 
		del items[items.index(item)]
	except:
		pass


def crop_str(text, a, b):
	u = len(a)
	v = len(b)*(-1)
	if text[:u] == a and text[v:] == b:
		text = text[u:]
		text = text[:v]
	return text


def selective_search(line, column=None, splitAt=None, index=None):
	final = None
	if column:
		final = get_nth_word(line, column)
	if splitAt:
		final = final.split(splitAt)
		if index: 
			final = final[index]
	return final
