from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
from enum import Enum

# IMPORT LOCAL
from account_backend.exceptions import *
from account_backend.tool import Signal, Account


__all__ = ("Actions", "ActionsNames")

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

# ACTIONS NAME
class ActionsNames(Enum):
    # USE ERROR SIGNAL
    BTN_LOGIN = 'login'
    BTN_CREATE_ACCOUNT = 'create_account'

class Actions:

    ERROR_SIGNAL = Signal()
    USERS_PATH = './accounts.json'

    def __init__(self) -> None:
        self._action_names = ActionsNames
        self._users: dict = Account(self.USERS_PATH, False)

    def btn_login(self, username: str, password: str) -> bool:
        print(f"BTN <LOGIN> IS CLICKED: [{username=}]\t[{password=}]")
        act_login_name = self._action_names.BTN_LOGIN

        if username.strip() == '' or password.strip() == '':
            self.ERROR_SIGNAL.emit(act_login_name, 'Feild Is Empty !')
            return False

        if self._users.check_account(username, password):
            return True

        self.ERROR_SIGNAL.emit(act_login_name, UserNameOrPasswordIsWrongError.__name__)
        return False


    def btn_create_account(self, username: str, password: str) -> bool:
        print(f'BTN <CREATE ACCOUNT> IS CLICKED: [{username=}]\t[{password=}]')
        act_login_name = self._action_names.BTN_CREATE_ACCOUNT
        try:
            self._users[username] = password
            self._users.save()
            return True
        except (UserNameAlreadyExists, PasswordIsNotValidError) as err:
            self.ERROR_SIGNAL.emit(act_login_name, type(err).__name__)
            return False


__dir__ = ("Actions", "ActionsNames")

