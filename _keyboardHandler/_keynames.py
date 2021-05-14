class _keynames():
       def get(self, key):
              arr = {
                     "enter": "[ENTER]\n",
                     "up": "[UP]\n",
                     "down" : "[DOWN]\n",
                     "space" : " ",
                     "shift" : "[SHIFT]",
                     "caps lock" : "\r",
                     "backspace" :  "[BACKSPACE]\n",
                     "tab" : "     ",
                     "alt" : "[ALT]",
                     "ctrl" : "[CTRL]\n"
              }
              return arr[key] if key in arr else False