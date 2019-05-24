from dotenv import load_env
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

