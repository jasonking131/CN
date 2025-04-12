try:
    import tomllib  # Python 3.11+
    with open('config.toml.sample', 'rb') as f:
        print(tomllib.load(f))
except ImportError:
    import toml
    print(toml.load('config.toml.sample'))