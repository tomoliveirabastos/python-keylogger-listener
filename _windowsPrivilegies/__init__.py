from os.path import realpath
from winreg import *
import os

class _windowsPriviligies():
       def _runWindows(self):
              path_arquivo = realpath(os.getcwd()+"\\..\\output\\__main__.exe")
              run = r'Software\\Microsoft\\Windows\\CurrentVersion\\Run'
              try:
                     key = OpenKey(HKEY_LOCAL_MACHINE, run, 0, KEY_SET_VALUE)
              except PermissionError:
                     print("nao tem permissao de adm", path_arquivo)
              else:
                     SetValueEx(key, 'PRGRAMA', 0,REG_SZ, path_arquivo)
                     key.Close()

_windowsPriviligies()._runWindows()