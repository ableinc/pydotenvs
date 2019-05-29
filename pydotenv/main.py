from os import environ, getcwd
import re, io, atexit, subprocess, shlex


class PyEnv:
	def __init__(self, env_path: str = '.env', stringIO: bool = False, auto_close: bool = False, verbose: bool = False):
		self.env_path = env_path
		self.stringIO = stringIO
		self.auto_close = auto_close
		self.verbose = verbose
		self.stringIOObject = None
		if self.auto_close:
			atexit.register(self.closer)

	def closer(self):
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

	def cli(self, command):
		env_file = self._read_env_file()
		try:
			for env in env_file:
				en_v = re.sub("['\"]", '', env.replace('\n', ''))
				idx = en_v.find('=')
				environ[str(en_v[:idx])] = str(en_v[idx+1:])
			if command or command != '':
				subprocess.run(shlex.split(command), cwd=getcwd(), env=environ.copy())
		except TypeError:
			print('TypeError: Invalid type in cli()')

	def load_env(self):
		env_file = self._read_env_file()
		if self.stringIO:
			return env_file
		try:
			for env in env_file:
				en_v = re.sub("['\"]", '', env.replace('\n', ''))
				idx = en_v.find('=')
				environ[str(en_v[:idx])] = str(en_v[idx+1:])
		except TypeError:
			print('TypeError: Invalid type in load_env()')

	def load_env_object(self):
		env_obj = {}
		env_file = self._read_env_file()
		try:
			for env in env_file:
				en_v = re.sub("['\"]", '', env.replace('\n', ''))
				idx = en_v.find('=')
				env_obj[str(en_v[:idx])] = str(en_v[idx+1:])
		except TypeError:
			print('TypeError: Invalid type in load_env_object()')
		return env_obj


def load_env(env_path: str = '.env', stringIO: bool = False, auto_close: bool = False, verbose: bool = False):
	return PyEnv(env_path, stringIO, auto_close, verbose).load_env()


def load_env_object(env_path: str = '.env', verbose: bool = False):
	return PyEnv(env_path, verbose=verbose).load_env_object()


def load_env_cli(env_path: str = '.env', command: str = '', verbose: bool = False):
	return PyEnv(env_path, verbose=verbose).cli(command)


def clear_env():
	environ.clear()
