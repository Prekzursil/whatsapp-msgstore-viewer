#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
WhatsApp Archive Viewer(WMV)
WMV is a free, open source and cross-platform app to decrypt, read and view the Whatsapp msgstore.db database.

(C) 2023 [absadiki](https://github.com/absadiki)

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "absadiki"
__copyright__ = "Copyright 2023"
__license__ = "GPLv3"
from version import __version__
__github__ = "https://github.com/absadiki/whatsapp-msgstore-viewer"

import importlib
import os
import sys

# pythonw/frozen runs have stderr/stdout=None; kivy logging on a None stream
# crashes at import. Redirect to devnull before anything kivy-side runs.
if getattr(sys, 'frozen', False) or sys.stderr is None or sys.stdout is None:
    if sys.stderr is None:
        sys.stderr = open(os.devnull, 'w')
    if sys.stdout is None:
        sys.stdout = open(os.devnull, 'w')


# Set KIVY_TEXT to pil to use the PIL text engine
os.environ['KIVY_TEXT'] = 'pil'

# App icon + taskbar identity (single owner: main.py). Absolute path derived
# from __file__ so the icon resolves regardless of the process CWD; the AUMID
# must match the one written into the Start Menu shortcut property store.
APP_DIR = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = os.path.join(APP_DIR, 'assets', 'images', 'app-icon.ico')
TASKBAR_IDENTITY_AUMID = "Prekzursil.WhatsAppArchiveViewer"

from kivy.resources import resource_add_path

from kivy import Config
from kivy.core.window import Window

resolution = Window.size
height = int(resolution[1] * 0.9)
# width = str(int(resolution[0]/3))

Config.set("graphics", "height", height)
Config.set("graphics", "width", '600')

from kivymd.tools.hotreload.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
import View.screens

importlib.reload(View.screens)
screens = View.screens.screens


class WhatsAppArchiveViewer(MDApp):
    KV_DIRS = [os.path.join(os.getcwd(), "View")]
    version = __version__
    g_page = __github__

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.msgstore_file = None
        self.wa_file = None
        self.wp_dir = None
        self.key = None

        self.default_settings = {
            'general_font': 'assets/fonts/Cairo.ttf',
            'emojis_font': 'assets/fonts/EmojiOneColor.otf',
            'call_log_size': 10
        }

        self.selected_chat_id = 0
        self.selected_user = ""
        self.selected_user_status = ""

        self.general_font = self.default_settings['general_font']
        self.emojis_font = self.default_settings['emojis_font']
        self.call_log_size = self.default_settings['call_log_size']

        self.db = None
        self.db_versions = []
        # pkgutil has issues when packaging the app

        # for _, name, _ in pkgutil.iter_modules(['./dbs']):
        #     if name != 'abstract_db':
        #         self.db_versions.append(name)

        # fix dynamically loading when packaging the app

        for dir_version in os.listdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dbs')):
            if dir_version.startswith('__') or dir_version.endswith('.py'):
                continue
            self.db_versions.append(dir_version)

        self.db_version = self.db_versions[0]

        self.screens_manager = MDScreenManager()

    def load_db(self):
        version = self.db_version
        db_module = f'dbs.{version}.db'
        db = importlib.import_module(db_module, package=None)
        self.db = db.Database(self.msgstore_file, self.wa_file)
        # checking schema, it will fail if the database schema is not supported
        self.db.check_database_schema()

        for i, name_screen in enumerate(screens.keys()):
            if name_screen == 'login screen':
                continue
            model = screens[name_screen]["model"](self.db)
            controller = screens[name_screen]["controller"](model)
            view = controller.get_view()
            view.screens_manager = self.screens_manager
            view.name = name_screen
            self.screens_manager.add_widget(view)

    def build_app(self) -> MDScreenManager:
        self.icon = ICON_PATH
        self.title = 'WhatsApp Archive Viewer'

        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.accent_palette = "Gray"
        self.theme_cls.accent_hue = '200'
        self.theme_cls.primary_dark_hue = '50'
        self.theme_cls.theme_style = 'Light'

        name_screen = 'login screen'
        model = screens[name_screen]["model"](self.db)
        controller = screens[name_screen]["controller"](model)
        view = controller.get_view()
        view.screens_manager = self.screens_manager
        view.name = name_screen
        self.screens_manager.add_widget(view)

        return self.screens_manager

    # Hot Reloading

    # Window.bind(on_key_down=self.on_keyboard_down)
    # def on_keyboard_down(self, window, keyboard, keycode, text, modifiers) -> None:
    #     """
    #     The method handles keyboard events.
    #
    #     By default, a forced restart of an application is tied to the
    #     `CTRL+R` key on Windows OS and `COMMAND+R` on Mac OS.
    #     """
    #
    #     if "meta" in modifiers or "ctrl" in modifiers and text == "r":
    #         self.rebuild()

def _set_taskbar_identity():
    """Set the process AppUserModelID via a hardened ctypes prototype.

    Returns the unsigned HRESULT (0x00000000 == S_OK). argtypes/restype are
    explicit and this MUST run before any Kivy window exists.
    """
    try:
        import ctypes
        shell32 = ctypes.windll.shell32
        shell32.SetCurrentProcessExplicitAppUserModelID.argtypes = [ctypes.c_wchar_p]
        shell32.SetCurrentProcessExplicitAppUserModelID.restype = ctypes.HRESULT
        return int(shell32.SetCurrentProcessExplicitAppUserModelID(TASKBAR_IDENTITY_AUMID)) & 0xFFFFFFFF
    except Exception:
        return 0xFFFFFFFF


def _write_launch_receipt(hr):
    """Append one startup receipt line: icon path, existence, AUMID HRESULT."""
    try:
        import time
        line = '%s pid=%s icon=%s iconExists=%s aumid=%s aumidHr=0x%08X\n' % (
            time.strftime('%Y-%m-%dT%H:%M:%S'), os.getpid(), ICON_PATH,
            os.path.exists(ICON_PATH), TASKBAR_IDENTITY_AUMID, hr)
        with open(r'D:\whatsapp-reunion\taskbar-verify\launch-receipt.log',
                  'a', encoding='utf-8') as fh:
            fh.write(line)
    except Exception:
        pass


def run():
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    # NOTE: the taskbar identity (AUMID) is set at module level below, before
    # WhatsAppArchiveViewer().run() creates the Kivy window. run_wmv.pyw no
    # longer sets its own AUMID (the first call per process wins, and the old
    # ".1" string there silently overrode this module's value).


# Hardened taskbar identity: single owner (main.py). Runs at import time,
# BEFORE any window creation, exactly as the API requires.
_AUMID_HRESULT = _set_taskbar_identity()
_write_launch_receipt(_AUMID_HRESULT)

WhatsAppArchiveViewer().run()


if __name__ == '__main__':
    run()
