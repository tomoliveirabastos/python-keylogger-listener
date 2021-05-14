import os
import platform
import requests
class _requestHandler():
       def __init__(self):
              pass
       def test(self):
              if not os.path.isfile("registerLog.txt"): return False
              file = open("registerLog.txt", 'rb')
              
              requests.post("http://localhost:5000", files={"upload_file": file}, params={
                     "osName" : os.name,
                     "platformName": platform.system()
              })
              file.close()
              
              os.remove("registerLog.txt")
              print("Request enviada")