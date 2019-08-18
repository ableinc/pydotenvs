from pydotenvs import load_env, load_env_object, clear_env
from os import getenv
from os.path import isfile

# write new .env file if not present
if not isfile('.env'):
    with open('.env', 'w+', encoding='utf-8') as write_env:
        write_env.writelines('HELLO=WORLD\nFOO=BAR')

# import library
load_env()
# print results
print(f'Hello Variable: {getenv("HELLO")} - Foo Variable: {getenv("FOO")}')
# clear local envs
print('Clearing envs. Confirming...')
clear_env()
# confirm envs are clear
if not getenv("HELLO"):
    print('No envs.')
else:
    print('Envs remain: ', getenv("HELLO"))
# Dictionary
print('Getting env as Dictionary...')
envDict = load_env_object()
print('Env Dict: ', envDict)
# StringIO Object
print('Getting env as StringIO Object...')
stringObj = load_env(stringIO=True, auto_close=True,
                     verbose=True)  # without auto close, you're resposible for closing StringIO object
contents = stringObj.getvalue()
print('StringIO Object Contents:\n', contents)
