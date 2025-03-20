import json
import os
import defaultConfig

class Config:
    config: dict = None

    def __init__(self) -> None:
        self.path = os.path.dirname(os.path.abspath(__file__))
        try:
            self.config: dict = json.load(open(os.path.join(self.path, "config.json")))
        except FileNotFoundError:
            # generate Default Config
            self.config: dict = defaultConfig.defaultConfig

    def get(self, key: str) -> str | None:
        if hasattr(self.config, key):
            return self.config[key]
        else:
            return None

    def set(self, key: str, value: str) -> bool:
        if hasattr(self.config, key):
            self.config[key] = value
            return True
        return False

    def save(self):
        with open(self.path + "/config.json", "w") as f:
            json.dump(self.config, f, indent=4)


def boostrap() -> Config:
    if not hasattr(Config, "__inst"):
        Config.__inst = Config()
    return Config.__inst


def get_config() -> Config:
    if hasattr(Config, "__inst"):
        return Config.__inst
    return boostrap()
