import Pyro4
import logging
import sys

class RPCServer(object):
    
    def __init__(self):
        from config import MalloryConfig
        # Make Pyro4 accept pickle again
        # https://github.com/irmen/Pyro4/blob/master/docs/source/clientcode.rst#upgrading-older-code-that-relies-on-pickle
        Pyro4.config.SERIALIZERS_ACCEPTED.add('pickle')

        self.daemon = Pyro4.Daemon(MalloryConfig.daemon_host, MalloryConfig.daemon_port, MalloryConfig.daemon_socket)
        self.log = logging.getLogger("mallorymain")
        
    def rpc_server(self):
        """
        rpcserver is intended to be launched as a separate thread. This class
        will launch an RPC server that can pass and receive debugging events
        to debugging clients.
        """

    def add_remote_obj(self, obj, name):
        # Register the Pyro object here
        self.log.info(("RPCServer: add_remote_obj - adding remote object %s " 
                      " with remote object name '%s'") % (obj, name))
        uri = self.daemon.register(obj, name)
        print "RPC: uri=", uri
        
    def start_server(self):
        self.log.info("RPCServer: start_server - starting up")     

        try:
            # Implicitly starts on port 7766. 
            # TODO: Make sure this listens on localhost only
            self.daemon.requestLoop()                    
        except:
            self.log.error("Failed to start the daemon")
            self.log.error(sys.exc_info())