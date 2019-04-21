import ctypes, sys, qDriverInstaller

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def runAsAdmin():
	if is_admin():
		qDriverInstaller.main()
	else:
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)