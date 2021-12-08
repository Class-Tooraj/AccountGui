from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
import os
import tkinter as tk
from enum import Enum

# IMPORT LOCAL
from account_backend.exceptions import *
from account_backend.tool import SignalThemeUpdate


__all__ = ('CustomTk', 'Themes', 'ThemeStyle')

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

"""
Themes:
    Use `Azure` & `Sun-Valley` Created By https://github.com/rdbende
"""


# THEMES PATH DICTIONARY
THEMES_PATH = {
    'azure': os.path.realpath('./themes/azure.tcl'),
    'sun-valley': os.path.realpath('./themes/sun-valley.tcl'),
    }

# THEMES SUPPORTS
class Themes(Enum):
    AZERU = 'azure'
    SUN_VALLEY = 'sun-valley'

# THEMES COLOR STYLE SUPPORTS
class ThemeStyle(Enum):
    DARK = 'dark'
    LIGHT = 'light'

# LOAD THEME STRING BYNARY FORMAT
def _load_theme(path) -> str:
    path = os.path.realpath(path)
    with open(path, 'rb') as f:
        return f.read()

# TK CUSTOMIZE APP
class CustomTk(tk.Tk):
    # Defaults Theme and ThemesStyle `ColorMode`
    _DEFAULT_THEME: Themes = Themes.AZERU
    _DEFAULT_STYLE: ThemeStyle = ThemeStyle.DARK

    # Signal Theme Updated After Update Theme or ThemeStyle This Signal Emitted
    # Connect This Signal if You Want Change or Edit Frames or Widgets See LoginFrame `theme_update` method
    # Connect This Signal Need Dictinary{name: method} or Iterable tuple(name, method)
    # Nothing Send To Method Only Called
    SIG_THEME_UPDATE = SignalThemeUpdate()

    # All Active Themes & Color Style Use Whwn Called Theme or ThemeStyle By Name
    THEMES_ACTIVE = {'azure': Themes.AZERU, 'sun_valley': Themes.SUN_VALLEY}
    COLOR_STYLE = {'dark': ThemeStyle.DARK, 'light': ThemeStyle.LIGHT}

    def __init__(self, theme: Themes | str = None, color_style: ThemeStyle | str = None,**kwargs) -> None:
        """[CustomTk instance Tk Whit Supporting Themes]

        Args:
            theme (Themes | str, optional): [Theme Use When Run]. Defaults to None means Azure.
            color_style (ThemeStyle | str, optional): [ThemeStyle Use When Run]. Defaults to None means Dark.
        """

        if isinstance(theme, str):
            theme = self.THEMES_ACTIVE.get(theme.lower(), None)

        if isinstance(color_style, str):
            color_style = self.COLOR_STYLE.get(color_style.lower(), None)

        self._theme = theme or self._DEFAULT_THEME
        self._style_active = color_style or self._DEFAULT_STYLE

        super(CustomTk, self).__init__(**kwargs)

        self._activate_theme()

    @property
    def color_style(self) -> ThemeStyle:
        """[Color Style Active]

        Returns:
            ThemeStyle: [ThemeStyle] ThemeStyle.DARK, ThemeStyle.LIGHT u need str name ThemeStyle.DARK.value
        """
        return self._style_active

    @color_style.setter
    def color_style(self, color_style: ThemeStyle | str) -> None:
        """[Set New ThemeStyle]

        Args:
            color_style (ThemeStyle | str): [Chose ThemeStyle With Type Or Name CaseSenstive is Off]
                Name: 'dark', 'light'

        Raises:
            StyleTypeError: [ThemeStyle Type Error]
        """
        if isinstance(color_style, ThemeStyle):
            self._style_active = color_style

        elif isinstance(color_style, str):
            self._style_active = self.COLOR_STYLE[color_style.lower()] if color_style.lower() in self.COLOR_STYLE else self._DEFAULT_STYLE

        else:
            raise StyleTypeError

        self._activate_style()

    @property
    def theme(self) -> Themes:
        """[Theme Active]

        Returns:
            Themes: [Themes] Themes.AZURE, Themes.SUN_VALLEY if need str name Themes.AZURE.value
        """
        return self._theme

    @theme.setter
    def theme(self, theme: Themes | str) -> None:
        """[Set Themes]

        Args:
            theme (Themes | str): [Set Themes By Type Or Names CaseSensitive is Off]
                Names: 'azure', 'sun_valley'

        Raises:
            ThemeTypeError: [description]
        """
        if isinstance(theme, Themes):
            self._theme = theme

        elif isinstance(theme, str):
            self._theme = self.THEMES_ACTIVE [theme.lower()] if theme.lower() in self.THEMES_ACTIVE else self._DEFAULT_THEME

        else:
            raise ThemeTypeError

        self._activate_theme()

    def _activate_style(self) -> None:
        # Activate Style Evry Time Change Color This Method Called
        # Use TCL Command For Set Style
        self.tk.call("set_theme", self._style_active.value)
        # Emited ThemeUpdate Signal
        self.SIG_THEME_UPDATE.emit()
        # Update App
        self.update()

    def _activate_theme(self) -> None:
        # Activate Themes First When Run Application This Method Called
        # Load Theme binaryString
        self._theme_string = _load_theme(THEMES_PATH[self._theme.value])
        # Use TCL Command For Execute String Theme
        self.tk.call("eval", self._theme_string)
        # Activate Style Called
        self._activate_style()
        # ThemeUpdate Signal Emited
        self.SIG_THEME_UPDATE.emit()
        # Update App
        self.update()

    def update_view(self, theme: str = None, style: str = None) -> None:
        # Update Theme or Style With Method
        # FIXME: Not Working If Theme Before Activated
        if style:
            self.theme_style = style
            self._activate_style()
        if theme:
            self.theme = theme
            self._activate_theme()


__dir__ = ('CustomTk', 'Themes', 'ThemeStyle')
