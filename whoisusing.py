#! /usr/bin/python3
from basicterminal import cli, get_first_argument, get_second_argument

psAux = 'ps aux '
pipe = ' | '
grep = 'grep '
binDir = '/bin/'
psAuxGrep = psAux + pipe + grep
binPsAuxBinGrep = binDir + psAux + pipe + binDir + grep
whoIsUsing = 'whoisusing'

knownList = [grep.replace(' ', ''), 
			 whoIsUsing, 
			 psAuxGrep,
			 binPsAuxBinGrep]

argShowLine = ['-l', '--line', 'l']

argShowPid = ['-p', '--pid', 'p']


def remove_byte_chars_from_str(text):
	if text[:2] == 'b\'':
		text = text[2:]
		text = text[:-1]
	return text


def get_first_word(text):
	return text.split(' ')[0]


def get_second_word(text):
	if len(text.split(' ')) > 1:
		for item in text.split(' ')[1:]:
			if item:
				return item


def remove_list_item_by_element(item, items):
	try: 
		del items[items.index(item)]
	except:
		pass


def add_to_pid_list(name, pid, pidDict):
	if name and name not in pidDict:
		pidDict[name] = []
	if name and pid not in pidDict[name]:
		pidDict[name].append(pid)


def add_to_user_list(user, users):
	if user and user not in users:
		users.append(user)


def add_all_users_to_list(lines, usersList, pidDict=None, exceptions=None):
	arg2 = get_second_argument()
	pid = ''
	knowns = knownList
	if exceptions:
		for exception in exceptions:
			remove_list_item_by_element(exception, knowns)
	for line in lines:
		nameTests = [name in line for name in knowns]
		if True in nameTests:
			pass
		else:
			user = get_first_word(line)
			add_to_user_list(user, usersList)
			if type(pidDict) == type({}):
				pid = get_second_word(line)
				add_to_pid_list(user, pid, pidDict)
			if arg2 in argShowLine:
				print(line)


def print_all(name, users, pidDict):
	test = ''
	try: test = users[0]
	except: pass
	if test:
		for i, user in enumerate(users):
			print(user, end	='\t')
			if pidDict:
				for pid in pidDict[user]:
					print(pid, end=' ')
			print()
	else:
		print('No user is currently using {}'.format(name))


def mod_name(name):
	return '/' + name


def who_is_using(name):
	if name:
		users = []
		pidDict = None
		exceptions = []
		command = psAuxGrep + mod_name(name)
		output = cli(command, printErrors=False)
		if output == None:
			command = binPsAuxBinGrep + mod_name(name)
			output = cli(command, printErrors=False)
		output = remove_byte_chars_from_str(output)
		output = output.split('\\n')
		if name in knownList:
			exceptions.append(name)
		if get_second_argument() in argShowPid:
			pidDict = {}
		add_all_users_to_list(output, users, pidDict=pidDict, exceptions=exceptions)
		print_all(name, users, pidDict)
	else:
		print('No name specified.')


who_is_using(get_first_argument())
