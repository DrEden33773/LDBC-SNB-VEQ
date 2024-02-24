import platform

wsl_if_on_windows = ["wsl"] if platform.system() == "Windows" else []
