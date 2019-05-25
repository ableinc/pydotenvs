# PY.Env
Environment variables for Python project
* Version Compatibility: Python 2 & 3

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
