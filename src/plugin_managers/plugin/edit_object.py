import config
from base import Base
import sys
from SimpleXMLRPCServer import SimpleXMLRPCServer
import xmlrpclib
from twisted.web import xmlrpc

class ObjectEditor (Base):
    
    def __init__(self, rules = [], config = config.Config()):
        Base.__init__(self)
        self.persistent = 1
        self.queue = []
        self.connected = False
        
    def do (self, **kwargs):
        #If noone is listening, just move along...
        if not self.connected:
            return kwargs
        
        # For now, we just store away the object in a queue. 
        # this enables the user to view the object, but not modify. 
        # Modifying objects using the objecteditor is the next step. 
        #
        object = kwargs['data']
        if  hasattr(object, "toDict"):
            self.pushobject(object.toDict())
        return kwargs

    def connect(self):
        """A UI calls this method via XMLRPC to tell the server that 
        it is listening for objects"""
        self.log.info("GUI connected")
        self.connected = True
        self.guiproxy = xmlrpclib.ServerProxy("http://localhost:20759")

    def pushobject(self, object):
        try:
            self.log.info("Pushing object to GUI")
            self.guiproxy.push(object)
        except xmlrpclib.Error, v:
            self.log.error(str(v))
            #Probably disconnect
            self.connected = False

    def runp(self):
        self.rpcserver()
        
    def rpcserver(self):
        """
        rpcserver is intended to be launched as a separate thread. This class
        will launch an RPC server that can pass and receive debugging events
        to debugging clients. 
        """      
        try:
            self.log.info("ObjectEditor: starting XML RPC Server")            
            server = SimpleXMLRPCServer(addr=("localhost", 20758), logRequests=False, allow_none=1)
            #server.register_function(self.disable, "")
            server.register_function(self.connect, "connect")
            server.serve_forever()
        except:
            self.log.error("ObjectEditor: rpcserver: error connecting to remote")
            self.log.error(sys.exc_info())

