import time
from threading import Thread

from _requestHandler import _requestHandler

class _workerHandler(Thread):
       def run(self):
              while True:
                     #_requestHandler().test()
                     time.sleep(60 * 3)
              pass