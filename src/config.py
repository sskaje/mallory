import logging
import sys
import json

class Config(object):
    def __init__(self):
        self.debug = 1
        self.http = {}
        self.http['flip_images'] = True
        
    def logsetup(self, log):
        """
        Static method use to configure the logging. Housed in the config
        class as it is a reasonable place to hold logging configuration 
        """
        fmt = "[*] [%(asctime)s] %(levelname)s:%(message)s"
    
        logging.basicConfig(filename="mallory.log",
                            filemode="w",
                            format=fmt)        
    
        console = logging.StreamHandler(sys.stdout)
        console.setLevel(logging.DEBUG)
        console.setFormatter(logging.Formatter(fmt))
        
        # Currently setup for debugging. Set this to logging.INFO to cut
        # down on the amount of logging detail.
        log.setLevel(logging.DEBUG)
        log.addHandler(console)
        
        log.info("Logging setup complete")


class MalloryConfigObject():
    def __init__(self, dict):
        for field in dict:
            setattr(self, field, dict[field])


class MalloryConfigVars():
    vars = ["listen", "dbname", "datadir"]

    def __init__(self):
        pass

    @staticmethod
    def get_vars():
        return MalloryConfigVars.vars


class MalloryConfig():
    debugger_uri = "PYROLOC://127.0.0.1:7766/debugger"
    config_protocols_uri = "PYROLOC://127.0.0.1:7766/config_proto"
    config_rules_uri = "PYROLOC://127.0.0.1:7766/config_rules"

    def __init__(self):
        pass

    @staticmethod
    def get_object():
        return MalloryConfigObject(MalloryConfig.get_dict())

    @staticmethod
    def get_dict():
        config = {}

        for field in MalloryConfigVars.get_vars():
            config[field] = MalloryConfig.get(field)

        return config

    @staticmethod
    def set_dict(dict):
        for field in dict:
            MalloryConfig.set(field, dict[field])

    @staticmethod
    def get_json():
        return json.dumps(MalloryConfig.get_dict())

    @staticmethod
    def set_json(json_string):
        dict = json.loads(json_string)
        MalloryConfig.set_dict(dict)

    @staticmethod
    def get(key):
        return getattr(MalloryConfig, key, "")

    @staticmethod
    def set(key, val):
        setattr(MalloryConfig, key, val)


