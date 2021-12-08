from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT LOCAL
from account_gui.login_gui import LoginFrame
from account_gui.custom_tk import CustomTk, Themes, ThemeStyle


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

"""
Themes & ThemeStyle
Theme Set:
    Themes.AZERU
    Themes.SUN_VALLEY
    or
    'azeru'
    'sun-valley'

Style Set:
    ThemeStyle.DARK
    ThemeStyle.LIGHT
    or
    'dark'
    'light'

Setup & Run CustomTk Themes Supports
    root = CustomTk(themes, style)
    or
    root = CustomTk() - Defaults Themes `Azure`, `Dark`
    -- Use `ttk` Widget For Support Themes
    tkwidget = ttk.Widget(root)
    -- Run App
    root.mainloop()
"""

# App is instance CustomTk
class App(CustomTk):
    pass

# Win is Instance LoginFrame - Login Frame Not is Child ttk.Frame is Custom Class Without Parrents
class LFrame(LoginFrame):
    pass


if __name__ == '__main__':

    # Use Theme By Name Or Themes Type
    # 2 Themes & 2 Color Styles Availble Default
    # Themes Name: `azure`, `sun-valley`
    # Color Style: `light`, `dark`
    # Default Run With `Azure` Themes & `Dark` Color Style

    # --- Setup & Run CustomTk ---
    # Setup `App` instance `CustomTk`
    # App(None, None) and App() = App(Themes.AZERU, ThemeStyle.DARK) or App('azure', 'dark')
    # Title & Icon & Other Root Configure Setup in Windows - See `LoginFrame`

    root = App()    # Default Theme Azure Dark

    # --- AZURE ---
    # Set by Type
    # root = App(Themes.AZURE, ThemeStyle.DARK)         # Azure Dark
    # root = App(Themes.AZURE, ThemeStyle.LIGHT)        # Azure Light
    
    # Set by Name
    # root = App('azure', 'dark')                       # Azure Dark
    # root = App('azure', 'light')                      # Azure Light

    # --- SUN_Valley ---
    # Set by Type
    # root = App(Themes.SUN_VALLEY, ThemeStyle.DARK)    # Sun-Valley Dark
    # root = App(Themes.SUN_VALLEY, ThemeStyle.LIGHT)   # Sun-Valley light

    # Set by Name
    # root = App('sun_valley', 'dark')                  # Sun-Valley Dark
    # root = App('sun_valley', 'light')                 # Sun-Valley light

    # Setup Widgets `LFrame` instance `LoginFrame`
    win = LFrame(root)

    # Run App
    raise SystemExit(root.mainloop())
