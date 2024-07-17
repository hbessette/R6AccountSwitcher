import ctypes
import os
import sys

if ctypes.windll.shell32.IsUserAnAdmin():
    temp = r"C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\temp_cache"
    p = r"C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\backup_cache"
    f = r"C:\Program Files (x86)\Ubisoft\Ubisoft Game Launcher\cache"
    
    # Check if directories exist before renaming
    if not (os.path.exists(p) and os.path.exists(f)):
        ctypes.windll.user32.MessageBoxW(0, "Folders are not found, rename folders to cache and backup_cache.", "Error", 16)
        sys.exit(1)

    try:        
        os.rename(f, temp)

        if os.path.exists(f):
            ctypes.windll.user32.MessageBoxW(0, "Ubisoft application is still running, go to task manager, end task, and retry.", "Error", 16)
        
        # Rename f to p (formerly p is now temp)
        os.rename(p, f)

        os.rename(temp, p)
        
        print("Source path renamed to destination path successfully.")
    
    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxW(0, "Folders are not found, rename folders to cache and backup_cache.", "Error", 16)
        sys.exit(1)
    
    except PermissionError:
        ctypes.windll.user32.MessageBoxW(0, "Ubisoft application is still running, go to task manager, end task, and retry.", "Error", 16)
        sys.exit(1)
    
    except OSError as e:
        ctypes.windll.user32.MessageBoxW(0, "Error occured, retry.", "Error", 16)
        sys.exit(1)
    
else:
    # If not admin, elevate privileges and run the script again
    ctypes.windll.shell32.ShellExecuteW(None, 'runas', sys.executable, os.path.abspath(__file__), None, 1)
