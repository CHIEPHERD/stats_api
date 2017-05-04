import os


class Environements:
    class __Environements:
        def __init__(self):
            file = open(".env", "r")
            envs = file.read().splitlines()

            for env in envs:
                if env == "":
                    continue
                key, value = env.split("=")
                if not key in os.environ:
                    os.environ[key] = value

        def get(self, key, default=None):
            try:
                return os.environ[key]
            except KeyError:
                return default

    instance = None

    def __new__(self):
        if not Environements.instance:
            Environements.instance = Environements.__Environements()
        return Environements.instance

    def __getattr__(self, attr):
        return getattr(self.instance, attr)

    def __setattr__(self, attr, val):
        return setattr(self.instance, attr, val)
