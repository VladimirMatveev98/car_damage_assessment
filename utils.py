import toml


def load_config(config_name):
    with open(config_name) as f:
        return toml.load(f)

