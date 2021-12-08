from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #



# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

class ThemeTypeError(TypeError):
    pass

class StyleTypeError(TypeError):
    pass

class UserNameAlreadyExists(NameError):
    pass

class PasswordIsNotValidError(ValueError):
    pass

class UserNameIsNotExistsError(KeyError):
    pass

class UserNameOrPasswordIsWrongError(KeyError, ValueError):
    pass

