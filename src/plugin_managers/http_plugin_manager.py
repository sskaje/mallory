
import config

import thread

from plugin_managers import base
from plugin.session_hijack import SessionHijack
from plugin.image_flip import ImageFlip
from plugin.image_invert import ImageInvert
from plugin_managers.plugin.edit_object import ObjectEditor
        
class HttpPluginManager (base.Base):
    def __init__(self, rules = [], config = config.Config()):
        base.Base.__init__(self)
        self.server_port = 80
        self.plugin_config()


    def plugin_config (self):
        #Make this more generic
        #Will support persistent, non persistent, plugins
        plugs = []
        plugs.append(SessionHijack ())
        plugs.append(ImageFlip())
        plugs.append(ImageInvert())
        plugs.append(ObjectEditor())
        #plugs.append(edit_object.ObjectEditor())
        for plug in plugs:
                if plug.persistent == 1:
                    thread.start_new_thread (plug.runp, ())
                self.plugins.append(plug)
