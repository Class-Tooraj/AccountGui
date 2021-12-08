from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
import os
import hashlib
import json

# IMPORT TYPING
from typing import Callable, Iterable, Any

# IMPORT LOCAL
from account_backend.exceptions import *

__all__ = ('Signal', 'SignalThemeUpdate', 'Account')

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #

# --- TYPE ALIAS ---

# -- SIGNAL THEME UPDATE --
# ^ MULTY ACTION THEME UPDATED TYPE ALIAS
_MULT_ACT_ITER = Iterable[tuple[str, Callable]]
_MULT_ACT_DICT = dict[str, Callable]
MULTI_ACTIONS = _MULT_ACT_ITER | _MULT_ACT_DICT



# Json Account
class Account(dict):
    """[Simple Account Manager Base On Json & Python dictinary]

    Args:
        path (str | os.PathLike): [Path User Json File] Default is None.
            if path is `None` Use `_DEFAULT_PATH = './users.json'`
        user_case_sensetive (bool): [UserName Case Sensetive] Default is False.

    Raises:
        UserNameAlreadyExists: [If Try Add UserName Alredy In Json]
        PasswordIsNotValidError: [If Password is not Valid]
        UserNameIsNotExistsError: [If Try Get UserName Not Exists in Json]

    """
    _DEFAULT_PATH: str = './accounts.json'

    def __init__(self, path: str | os.PathLike = None, user_case_sensetive: bool = False) -> None:
        super(Account, self).__init__()
        self._path = os.path.realpath(path) if path is not None else os.path.realpath(self._DEFAULT_PATH)
        self._user_case = user_case_sensetive

    def _ready(self) -> None:
        if os.path.isfile(self._path):
            self._read()
        else:
            self.refresh()

    def _read(self) -> None:
        self.clear()
        with open(self._path, 'r') as f:
            self.update(json.load(f))

    def _write(self) -> None:
        with open(self._path, 'w') as f:
            json.dump(self, f)

    def save(self) -> None:
        self._write()

    def refresh(self) -> None:
        self._write()
        self._read()

    def __setitem__(self, username: str, password: str) -> None:
        if not self._user_case:
            username = username.lower()

        if username in self:
            raise UserNameAlreadyExists

        if not self.password_valid(password):
            raise PasswordIsNotValidError

        password = self.secure(password)

        super(Account, self).__setitem__(username, password)

    def __getitem__(self, username: str) -> str:
        if not self._user_case:
            username = username.lower()

        try:
            return super(Account, self).__getitem__(username)
        except KeyError:
            raise UserNameIsNotExistsError 

    def get(self, username: str, alt: object = None) -> str | object:
        if not self._user_case:
            username = username.lower()

        return super(Account, self).get(username, alt)

    def check_account(self, username: str, password: str) -> bool:
        get = self.get(username, None)
        if get is None:
            return False

        if self.secure(password) == get:
            return True

        return False

    def update(self, updateval: dict[str, str] | Iterable[tuple[str, str]]) -> None:
        valid_user = lambda x: x.lower() if not self._user_case else x
        if isinstance(updateval, dict):
            updateval = {valid_user(username): self.secure(password) for username, password in updateval.items()}
        else:
            updateval = {valid_user(username): self.secure(password) for username, password in updateval}
        super(Account, self).update()

    @staticmethod
    def password_valid(password: str) -> bool:
        if len(password) < 6:
            return False
        return True

    @staticmethod
    def secure(inp: str) -> str:
        return hashlib.sha256(inp.encode('utf-8')).hexdigest()


# SIGNAL
class Signal:
    """[Basic Signal Classes]
    """
    def __init__(self) -> None:
        self._connect = None

    @property
    def connect(self) -> Callable:
        return self._connect

    @connect.setter
    def connect(self, action: Callable) -> None:
        self._connect = action

    def emit(self, *args, **kwargs) -> Any:
        if self.connect is None:
            return None
        return self._connect(*args, **kwargs)


# THEME CHANGE SIGNAL
class SignalThemeUpdate(Signal):
    """[Signal Only Calling Without Any Arguments & Supprot Multi Connection With Dictionary]

    Args:
        Signal ([type]): [description]
    """

    def __init__(self) -> None:
        super(SignalThemeUpdate, self).__init__()
        self._connect: dict[str, Callable] = {}

    @property
    def connect(self) -> dict[str, Callable]:
        """[connected]

        Returns:
            dict[str, Callable]: [Dictionary Of Connected Methods]
            pattern: {name: method, ...}
        """
        return self._connect

    @connect.setter
    def connect(self, acions: MULTI_ACTIONS) -> None:
        """[Connect Your Calling Actions]

        Args:
            acions (MULTI_ACTIONS): [Action Or Actions Must Be Iterable or Dictionary]
                example_1 : sig_theme_updated = [(name, `callable` method), ...]
                example_2 : sig_theme_updated = {name: `callable`, ...}
        """
        if isinstance(acions, dict):
            self._connect.update(acions)
        else:
            actions_to_dict = {key: value for key, value in acions}
            self._connect.update(actions_to_dict)

    @connect.deleter
    def connect(self, name_names: str | Iterable[str]) -> None:
        """[Remove Connected Method or Methods]

        Args:
            name (str | Iterable[str]): [Remove Method Connected By Name or Names for Multi Remove]
        """
        if isinstance(name_names, str):
            del self._connect[name_names]
        elif isinstance(name_names, Iterable):
            for name in name_names:
                del self._connect[name]

    def emit(self) -> None:
        """[emitted Signal Means Theme Updated Any changes Update And This Method Calling]
        """
        for action in self._connect.values():
            action()



__dir__ = ('Signal', 'SignalThemeUpdate', 'Account')
