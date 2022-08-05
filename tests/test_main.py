from pydotenvs.main import load_env, load_env_object
import unittest
import os.path
from os import curdir, environ
from io import StringIO

env_file_path = os.path.abspath(curdir) + '/tests/.env-test'

class TestPyEnv(unittest.TestCase):
    def test_load_env(self):
        load_env(env_file_path)
        self.assertEqual(environ.get('APP_NAME'), 'pydotenvs')
        self.assertEqual(environ.get('AUTHOR'), 'ableinc')

    def test_load_env_object(self):
        obj = load_env_object(env_file_path)
        self.assertIsNotNone(obj)
        self.assertIsInstance(obj, dict)
        self.assertListEqual([x for x in obj.keys()], ['APP_NAME', 'AUTHOR', 'HELLO', 'ARRAY', 'DICT', 'NOT_DICT', 'INT', 'FLOAT', 'UNWANTED_TABLES'])
    
    def test_load_env_string_io(self):
        self.assertWarns(ResourceWarning, load_env, env_file_path, True, True)
        string_io = load_env(env_file_path, stringIO=True, auto_close=True)
        self.assertIsInstance(string_io, StringIO)

    def test_load_env_object_error(self):
        self.assertRaises(TypeError, load_env_object, '.not-real-file-path')


if __name__ == '__main__':
    unittest.main()
