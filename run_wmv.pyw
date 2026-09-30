"""No-console launcher (pythonw) for WhatsApp Archive Viewer.

pythonw.exe provides no stdout/stderr (they are None); main.py's shim
redirects them to devnull so Kivy logging never crashes on a missing stream.
"""
import os
import sys

# Explicit AppUserModelID: makes the taskbar use the window icon + our
# grouping instead of pythonw.exe's generic python icon. Must run BEFORE
# kivy creates the window (i.e. before importing main).
if sys.platform == "win32":
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("Prekzursil.WhatsAppArchiveViewer.1")

here = os.path.dirname(os.path.abspath(__file__))
os.chdir(here)
sys.path.insert(0, here)

from main import run

run()
