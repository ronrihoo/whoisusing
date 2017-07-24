import sys
import subprocess

logging = False


# LOGGING


def set_logging(state):
	logging = state


# TERMINAL


def get_first_argument():
	arg = ''
	try:
		arg = sys.argv[1]
	except:
		arg = ''
	return arg


def get_second_argument():
	arg = ''
	try:
		arg = sys.argv[2]
	except:
		arg = ''
	return arg


def get_all_arguments():
	if len(sys.argv) > 1:
		return sys.argv[1:]
	return []


def handle_argument(arg, trigger='-'):
	if trigger in arg and trigger == '-': 
		# do something different here
		print('{} '.format(arg), end='')
	else: 
		print('{} '.format(arg), end='')


def cli(cmd, printErrors=True):
	if logging: 
		print('opening ' + cmd[0], end=': ')
		[handle_argument(arg) for arg in cmd[1:]]
	output = run_with_popen(cmd)
	if not printErrors:
		output = validate_output(output)
	return output


def run_with_popen(command):
	if logging: print('waiting for response from subprocess')
	out = ''
	err = ''
	output = subprocess.Popen(command, 
							  shell=True, 
							  stdout=subprocess.PIPE, 
							  stderr=subprocess.PIPE)
	out, err = output.communicate()
	if err:
		return str(err)
	else:
		return out


def run_and_get_output(cmd):
	if logging: print('waiting for response from subprocess')
	cmd = list_to_str(cmd)
	try:
		output = subprocess.check_output(cmd, 
										 shell=True, 
										 stderr=subprocess.STDOUT) \
			.decode("utf-8") \
			.strip()
	except:
		output = ''
	return output


# OUTPUT


def validate_output(output):
	'''
		Checks for known problems

		Args:
			output (str): this is expected to be the string output returned by 
				subprocess

		Returns: 
			None: where a problem is identified, None is returned
			Str: where no problems are identified, the argument is returned
	'''
	bin_sh = '/bin/sh'
	not_found = 'not found'
	if type(output) != type(''):
		output = str(output)
	if bin_sh in output and not_found in output:
		return None
	return output


# CONVERTERS


def list_to_str(obj):
	if type(obj) == type([]):
		obj = ' '.join(obj)
	return obj


def str_to_list(obj):
	if type(obj) == type(''):
		obj = obj.split(' ')
	return obj

