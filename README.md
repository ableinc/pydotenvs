# PY.Env
Import environment variables from your .env file or run as command line tool; PyDotEnv Cli.
* Python 2 & 3
* Command line tool

# Version
Stable: v0.1.5

# How to use
```bash
pip install pydotenvs

or 

git clone https://github.com/ableinc/pyenv.git
cd pyenv
pip install --editable .
```
Now import into any python project you have <br />
``` python
from pydotenvs import load_env
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
python example/demo.py
``` 

# StringIO
You can load your local .env file as a StringIO object. 
By default you are responsible for closing the StringIO
object. Though, there is an option to auto close upon program
termination.

```python
from pydotenvs import load_env
stringObj = load_env(stringIO = True, auto_close = True)
contents = stringObj.getvalue()
```

# Transfer
You can now transfer an existing .env file variables to a new .env file,
with the option of preserving or overriding the existing values in the new
.env file. You can use this feature via the CLI tool or by importing the
function from the pydotenvs library. Preserve is True by default. Example:
```python
from pydotenvs import transfer_new_env, load_env
transfer_new_env(old_env_path = '.env', new_env_path = '.env-new', preserve = True)
# load_env('.env-new')
```
or
```bash
pyenv -f .env -n .newenv -t True
```

# Command Line Tool - CLI
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
  -n, --newpath PATH      Location of new .env file that you would like to
                          transfer old env file variables to
  -t, --transfer BOOLEAN  This must be true if you would like to transfer.
                          --newpath is required as well.
  -p, --preserve BOOLEAN  True or False whether or not to preserve existing
                          envs during transfer
  -c, --command TEXT      Run a command that requires local enviornment
                          variables for one instance
  -l, --loadobj BOOLEAN   Load .env file as object instead of environment
                          variable
  -s, --stringio BOOLEAN  Load .env file as StringIO object instead of
                          environment variable
  -v, --verbose BOOLEAN   Verbose
  --version               Show the version and exit.
  --help                  Show this message and exit.
  ```

# Changelog
* January 2022 - Minfor version update
  - You can now transfer an old .env file document to a new .env file document. Described above.
  - Before, the .env file was required at root of the project directory. This is no longer the case, you
    can now give any file path on the system.
* October 2020 - Minor version update
  - Any message that should/shall be printed (unrelated to an error) will be controlled by the boolean value of verbose.
  - Cleaned the CLI code, slightly
