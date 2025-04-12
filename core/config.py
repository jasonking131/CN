import os
try:
    import tomllib
except ImportError:
    import toml as tomllib

class Config:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), '../../config.toml')
        with open(config_path, 'rb') as f:
            self.data = tomllib.load(f)
    
    def get(self, section, key):
        return self.data.get(section, {}).get(key)