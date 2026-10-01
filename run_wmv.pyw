"""No-console launcher (pythonw) for WhatsApp Archive Viewer.

pythonw.exe provides no stdout/stderr (they are None); main.py's shim
redirects them to devnull so Kivy logging never crashes on a missing stream.
"""
import os
import sys

# AppUserModelID is owned by main.py (_set_taskbar_identity: hardened ctypes
# prototype with the exact AUMID the Start Menu shortcut carries). Do NOT set
# it here: the FIRST SetCurrentProcessExplicitAppUserModelID call per process
# wins, and the old ".1" string here silently overrode main.py's value
# (measured 2026-10-01: taskbar fell back to pythonw.exe branding "Python").

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)
sys.path.insert(0, here)

from main import run

run()
