# administrative help
from basicterminal import cli


def where_am_i():
	dirs = (str(cli('whereis whoisusing')).replace('\'', '').replace('\\n', ''))[1:].split(' ')[1:]
	for d in dirs:
		if d:
			print(d)


def find_me():
	dirs = (str(cli('find / -name "whoisusing" 2>/dev/null')).replace('\'', ''))[1:].split('\\n')
	for d in dirs:
		if d:
			print(d)
