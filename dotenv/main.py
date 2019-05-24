from os import environ

def load_env(env_path: str = '.env'):
    env_file = open(env_path, 'r').readlines()
    for env in env_file:
        en_v = env.replace('\n', '')
        idx = en_v.find('=')
        environ[str(en_v[:idx])] = str(en_v[idx+1:])