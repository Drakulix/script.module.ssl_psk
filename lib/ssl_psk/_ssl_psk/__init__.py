from sys import platform as _platform

if _platform == "linux" or _platform == "linux2":
    from ._ssl_psk_lin import *
elif _platform == "darwin":
    from ._ssl_psk_osx import *
elif _platform == "win32":
    from ._ssl_psk_win import *
