#! /usr/bin/python3
from basicterminal import cli, get_first_argument, get_second_argument
from basicparser import get_first_word, get_nth_word, validate_input, \
	remove_list_item_by_element, crop_str, selective_search, get_matched_lines
from adminhelp import where_am_i, find_me

psAux = 'ps aux '
binDir = '/bin/'
binPsAux = binDir + psAux
whoIsUsing = 'whoisusing'

knownList = [whoIsUsing, 
			 binPsAux]

argShowLine = ['-l', '--line', 'l']

argShowPid = ['-p', '--pid', 'p']

argFindMe = ['--whereami', '--findme']


def handle_argument_flags(arg):
	if '--' in arg:
		if arg == '--findme':
			find_me()
			return True
		elif arg == '--whereami':
			where_am_i()
			return True
	return False


def get_process_list_from_shell():
	command = psAux
	output = cli(command, printErrors=False)
	if output == None:
		command = binPsAux
		output = cli(command, printErrors=False)
	return output


def get_refined_process_list(name):
	output = get_process_list_from_shell()
	output = crop_str(output, 'b\'', '\'')
	return get_matched_lines(output, name)


def build_ignore_list(exceptions=[]):
	if name in knownList:
		exceptions.append(name)
	return exceptions


def get_actual_name(line):
	return selective_search(line, column=11, splitAt='/', index=-1)


def verify_line(line, text):
	actualName = get_actual_name(line)
	if text == actualName or text + 'd' == actualName:
		return True
	return False


def get_lines_with_actual_name(lines, name):
	refined = []
	for line in lines:
		if verify_line(line, name):
			refined.append(line)
	return refined


def add_to_list_in_dict(key, value, dictionary):
	if key and key not in dictionary:
		dictionary[key] = []
	if key and value not in dictionary[key]:
		dictionary[key].append(value)


def add_to_user_list(user, users):
	if user and user not in users:
		users.append(user)


def add_all_users_to_list(lines, 
						  usersList, 
						  actualDict=None, 
						  pidDict=None, 
						  dirDict=None, 
						  lineList=None, 
						  exceptions=None):
	pid = ''
	knowns = knownList
	showActual = (type(actualDict) == type({}))
	keepPid = (type(pidDict) == type({}))
	keepDir = (type(dirDict) == type({}))
	keepLine = (type(lineList) == type([]))
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
			if showActual:
				actual = get_actual_name(line)
				add_to_list_in_dict(user, actual, actualDict)
			if keepPid:
				pid = get_nth_word(line, 2)
				add_to_list_in_dict(user, pid, pidDict)
			if keepDir:
				directory = get_nth_word(line, 11)
				add_to_list_in_dict(user, directory, dirDict)
			if keepLine:
				lineList.append(line)


def print_all(name, users, actualDict, pidDict, dirDict, lineList):
	if lineList:
		for line in lineList:
			print(line)
		print()
	if len(users) > 0:
		for i, user in enumerate(users):
			end = '\t'
			print(user, end=end)
			if actualDict:
				for i, actual in enumerate(actualDict[user]):
					print(actual, end=' ')
					if pidDict:
						print(pidDict[user][i], end= ' ')
			if pidDict and not actualDict:
				for pid in pidDict[user]:
					print(pid, end=' ')
			if dirDict:
				if pidDict:
					print(end='\n\t')
				for directory in dirDict[user]:
					print(directory, end = ' ')
			print()
	else:
		print('No user is currently using {}'.format(name))


def who_is_using(name):
	users = []
	actualDict = None
	pidDict = None
	dirDict = None
	lineList = None
	output = get_refined_process_list(name)
	#ignore = build_ignore_list(): # add_all_users_to_list(..., exceptions=ignore)
	if 's' in get_second_argument():
		output = get_lines_with_actual_name(output, name)
	if 'a' in get_second_argument():
		actualDict = {}
	if 'p' in get_second_argument():
		pidDict = {}
	if 'd' in get_second_argument():
		dirDict = {}
	if 'l' in get_second_argument():
		lineList = []
	add_all_users_to_list(output, 
						  users, 
						  actualDict=actualDict, 
						  pidDict=pidDict, 
						  dirDict=dirDict, 
						  lineList=lineList)
	print_all(name, users, actualDict, pidDict, dirDict, lineList)


def main(arg):
	if handle_argument_flags(arg):
		pass
	elif arg and validate_input(arg):
		who_is_using(arg)
	elif not arg and not validate_input(arg):
		print('No name specified')
	else:
		print('Invalid input')


main(get_first_argument())
