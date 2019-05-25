import click, os
from pydotenv.main import load_env_cli, load_env, load_env_object
from pydotenv.version import __version__


@click.command('pydotenv')
@click.option('-f', '--envpath', required=1, default=os.path.join(os.getcwd(), '.env'), type=click.Path(exists=True), help='Location of .env file, defaults to .env in current working directory')
@click.option('-c', '--command', type=click.STRING, help='Run a command that requires local enviornment variables for one instance')
@click.option('-l', '--loadobj', default=False, type=click.BOOL, help='Load .env file as object instead of environment variable')
@click.option('-s', '--stringio', default=False, type=click.BOOL, help='Load .env file as StringIO object instead of environment variable')
@click.option('-v', '--verbose', default=False, type=click.BOOL, help='Verbose')
@click.option('-i', '--ignore', default=False, type=click.BOOL, help='Ignore special characters in variable values')
@click.version_option(version=__version__)
def pyenv(envpath, command, loadobj, stringio, verbose, ignore):
	if stringio:
		stringObj = load_env(env_path=envpath, stringIO=stringio, auto_close=True, verbose=verbose)  # without auto close, you're resposible for closing StringIO object
		print(stringObj.getvalue())
	if loadobj:
		envDict = load_env_object(env_path=envpath, verbose=verbose)
		print(envDict)
	# if neither above are true do as normal
	load_env_cli(env_path=envpath, command=command, verbose=verbose, ignoreChars=ignore)


if __name__ == '__main__':
	pyenv()
