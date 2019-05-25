# PY.Env
Adds environment variables from your .env file
* Python 2 & 3
* Command line tool

# How to use
```git clone https://github.com/ableinc/pyenv.git``` <br />
```cd pyenv``` <br />
```pip install .``` <br />
Now import into any python project you have <br />
```from dotenv import load_env```<br />
```load_env()```<br />
or<br />
```load_env('.myEnvFile')```<br />
or <br />
```envObj = load_env_object()```<br />
```envObj['myEnv']```<br />
That's it!

# Test
Please run ```python test.py``` to see a working example

# StringIO
You can load your local .env file as a StringIO object. 
By default you are responsible for closing the StringIO
object. Though, There is an option to auto close upon program
termination.

```stringObj = load_env(stringIO = True, auto_close = True)```<br />
```contents = stringObj.getvalue()```

# Command Line Tool
You can use PyEnv as a command line tool. All the same features apply.
It would be common to use the client tool for the Dictionary & StringIO 
features of PyEnv.

You can run a command that requires your local enviornment variables
with PyEnv command line tool. Your variables will only exist in 
that one instance.
i.e. ```python --command 'echo $MY_VARIABLE'```

Usage: cli.py [OPTIONS]

Options:
  -f, --envpath PATH       Location of .env file, defaults to .env in current
                           working directory  [required]
  -c, --command TEXT       Run a command that requires local enviornment
                           variables for one instance
  -l, --loadobj BOOLEAN    Load .env file as object instead of environment
                           variable
  -s, --stringio BOOLEAN   Load .env file as StringIO object instead of
                           environment variable
  -a, --autoclose BOOLEAN  Auto-close StringIO object
  -v, --verbose BOOLEAN    Verbose
  -i, --ignore BOOLEAN     Ignore special characters in variable values
  --version                Show the version and exit.
  --help                   Show this message and exit.
