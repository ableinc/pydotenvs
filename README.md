# PY.Env
Import environment variables from your .env file or run as command line tool; PyDotEnv Cli.
* Python 2 & 3
* Command line tool

# How to use
```bash
pip install pydotenvs

or 

git clone https://github.com/ableinc/pyenv.git
cd pyenv
pip install --upgrade .
```
Now import into any python project you have <br />
``` python
from dotenv import load_env
load_env()
```
or <br />
```python 
load_env('.myEnvFile')
```
or <br />
```python 
envObj = load_env_object()
envObj['myEnv']
```
That's it!

# Test
Run this to see a working example
```python
python test.py
``` 

# StringIO
You can load your local .env file as a StringIO object. 
By default you are responsible for closing the StringIO
object. Though, There is an option to auto close upon program
termination.

```python
stringObj = load_env(stringIO = True, auto_close = True)
contents = stringObj.getvalue()
```

# Command Line Tool
You can use PyEnv as a command line tool. All the same features apply.
It would be common to use the client tool for the Dictionary & StringIO 
features of PyEnv.

You can run a command that requires your local environment variables
with PyEnv command line tool. Your variables will only exist in 
that one instance.

```bash
 pyenv --command 'echo $MY_VARIABLE'
 ```

```bash
Usage: pyenv [OPTIONS]

Options:
  -f, --envpath PATH      Location of .env file, defaults to .env in current
                          working directory  [required]
  -c, --command TEXT      Run a command that requires local enviornment
                          variables for one instance
  -l, --loadobj BOOLEAN   Load .env file as object instead of environment
                          variable
  -s, --stringio BOOLEAN  Load .env file as StringIO object instead of
                          environment variable
  -v, --verbose BOOLEAN   Verbose
  -i, --ignore BOOLEAN    Ignore special characters in variable values
  --version               Show the version and exit.
  --help                  Show this message and exit.
  ```

