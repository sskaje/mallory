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
    def __init__(self, dic):
        for field in dic:
            setattr(self, field, dic[field])


class MalloryConfigVars():
    vars = ["listen", "dbname", "datadir"]

    def __init__(self):
        pass

    @staticmethod
    def get_vars():
        return MalloryConfigVars.vars


class MalloryConfig():
    def __init__(self):
        pass

    daemon_host = "127.0.0.1"
    daemon_port = 7766
    daemon_socket = None

    debugger = "debugger"
    config_proto = "config_proto"
    config_rules = "config_rules"
    pyro_objs = [debugger, config_proto, config_rules]

    @staticmethod
    def get_pyro_uri(key):
        """
        Build Pyro4 URI from local config both HOST:PORT and Unixsocket are supported
        """
        prefix = "PYRO:"
        if MalloryConfig.daemon_socket is None:
            uri = MalloryConfig.daemon_host + ":" + str(MalloryConfig.daemon_port)
        else:
            uri = "./u:" + MalloryConfig.daemon_socket

        if key in MalloryConfig.pyro_objs:
            return prefix + key + "@" + uri

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
    def set_dict(dic):
        for field in dic:
            MalloryConfig.set(field, dic[field])

    @staticmethod
    def get_json():
        return json.dumps(MalloryConfig.get_dict())

    @staticmethod
    def set_json(json_string):
        dic = json.loads(json_string)
        MalloryConfig.set_dict(dic)

    @staticmethod
    def get(key):
        return getattr(MalloryConfig, key, "")

    @staticmethod
    def set(key, val):
        setattr(MalloryConfig, key, val)


