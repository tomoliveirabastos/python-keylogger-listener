from _keyboardHandler import _keyboardHandler
from _requestHandler import _requestHandler
from _workerHandler import _workerHandler

import time
if __name__ == "__main__" :
       _workerHandler().start()
       _keyboardHandler().initialize()