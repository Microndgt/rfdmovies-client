import os
import yaml


def _self_path():
    if '__file__' in globals():
        return __file__
    import rfdmovie
    return rfdmovie.__file__.replace('__init__', 'config')


project_root = os.path.dirname(os.path.dirname(os.path.abspath(_self_path())))
_config_file = '{}/config/config-{}.yml'.format(project_root, os.environ.get('ENV') or 'dev')
_config_data = None
_confusion = False
env_config_prefix = 'RFDMOVIE_CONFIG_'

PREDEFINED_VARS = {
    "project_root": project_root,
}


def init():
    global _config_file
    if os.path.isfile(_config_file):
        return
    else:
        raise Exception("Must provide config: {}".format(_config_file))


init()


def path(*args):
    return os.path.join(project_root, *args)


def load_config(path=None):
    global _config_data
    if _config_data:
        return

    path = path or _config_file
    _config_data = yaml.load(open(path))


def fill_vars(value):
    if isinstance(value, str):
        value = value.format(**PREDEFINED_VARS)
    return value


def get_config(key_string="", default=None):
    env_name = '{}{}'.format(env_config_prefix, key_string.replace('.', '_').upper())
    if env_name in os.environ:
        ret = os.getenv(env_name)
    else:
        load_config()
        keys = [key.strip() for key in key_string.split(".") if key]
        ret = _config_data
        for key in keys:
            ret = ret.get(key)
            if ret is None:
                return fill_vars(default)
    return fill_vars(ret)

