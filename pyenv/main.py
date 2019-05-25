from os import environ
import re, io, atexit


class PyEnv:
	def __init__(self, env_path: str = '.env', stringIO: bool = False, auto_close: bool = False, verbose: bool = False):
		self.env_path = env_path
		self.stringIO = stringIO
		self.auto_close = auto_close
		self.verbose = verbose
		self.stringIOObject = None
		if self.auto_close:
			atexit.register(self.printer)

	def printer(self):
		if self.stringIOObject:
			if self.verbose:
				print('Auto-closing StringIO Object')
			self.stringIOObject.close()

	def _read_env_file(self):
		if not self.stringIO:
			try:
				return open(self.env_path, 'r', encoding='utf-8').readlines()
			except TypeError:
				print('Invalid file type.')
				return
			except FileNotFoundError:
				print('Unable to find file.')
				return
		self.stringIOObject = io.StringIO()
		env_file = io.open(self.env_path, mode='r', encoding='utf-8').read()
		self.stringIOObject.write(env_file)
		return self.stringIOObject

	def load_env(self):
		env_file = self._read_env_file()
		if self.stringIO:
			return env_file
		for env in env_file:
			en_v = env.replace('\n', '')
			idx = re.sub(r'[-!@_""*&^%$#)(]', "", en_v).find('=')
			environ[str(en_v[:idx])] = str(en_v[idx+1:])

	def load_env_object(self):
		env_obj = {}
		env_file = self._read_env_file()
		for env in env_file:
			en_v = env.replace('\n', '')
			idx = re.sub(r'[-!@_""*&^%$#)(]', "", en_v).find('=')
			env_obj[str(en_v[:idx])] = str(en_v[idx+1:])
		return env_obj

def load_env(env_path: str = '.env', stringIO: bool = False, auto_close: bool = False, verbose: bool = False):
	return PyEnv(env_path, stringIO, auto_close, verbose).load_env()

def load_env_object(env_path: str = '.env', verbose: bool = False):
	return PyEnv(env_path, verbose=verbose).load_env_object()

def clear_env():
	environ.clear()
