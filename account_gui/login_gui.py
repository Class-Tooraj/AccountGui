from __future__ import annotations
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> #
#           < IN THE NAME OF GOD >           #
# ------------------------------------------ #
__AUTHOR__ = "ToorajJahangiri"
__EMAIL__ = "Toorajjahangiri@gmail.com"
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< #


# IMPORT
from tkinter import PhotoImage
from tkinter import ttk
from tkinter import messagebox

# IMPORT LOCAL
from account_gui.custom_tk import CustomTk
from account_backend.actions import Actions, ActionsNames


__all__ = ('LoginFrame',)

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\^////////////////////////////// #


# LOGIN FRAME
class LoginFrame:
    # --- ICON PATH ---
    _ICON: str = './icon.ico'

    # --- AVATARS PATH ---
    # Light Theme Syle Avatar
    _LIGHT_STYLE_AVATAR: str = './img/avatar_light_theme_100x100.png'

    # Dark Theme Syle Avatar
    _DARK_STYLE_AVATAR: str = './img/avatar_dark_theme_100x100.png'

    # Buttons & Label Text
    # NOTE: Change This If Need Custom Texts
    TEXTS = {
        'win_title': 'Account',     # Root Title Text
        'lbl_logo': 'Login',        # Big Text Logo Top Center Text
        'lbl_username': 'UserName', # UserName Entry Label Text
        'lbl_password': 'Password', # Password Entry Labed Text
        'lbl_comments': 'This is a Comments',   # Comments Label Text
        'lbl_about': 'Account Gui - v 0.1',     # About Label Text
        'btn_login': 'Login',       # Login Button Text
        'btn_clear': 'Refresh',     # Clear Button Text
        'btn_create_account': 'Create Account', # Create Account Button Text
        'cbtn_color_reverse': 'Color Reverse',  # Change Color Check Button Text
        }

    # Labels Color 3 Label Colored Logo Label & Comments Label & About Label
    COLOR_LABELS = {
        'lbl_logo': {'dark': '#408add', 'light': '#123d54'},
        'lbl_comments': {'dark': '#408add', 'light': '#123d54'},
        'lbl_about': {'dark': '#606060', 'light': '#7f7f7f'},
    }

    def __init__(self, master: CustomTk) -> None:
        """[Login Gui]

        Args:
            master (ROOT): [Tkinter Tk Root Screen Must Be `CustomTk` For Theme Supports]
        """
        # Load Avatar Styles From Avatar Files to Memory
        self._avatars_data = {}
        with (
            open(self._LIGHT_STYLE_AVATAR, 'rb') as f_avatar_light,
            open(self._DARK_STYLE_AVATAR, 'rb') as f_avatar_dark,
            ):
            self._avatars_data['light'] = f_avatar_light.read()
            self._avatars_data['dark'] = f_avatar_dark.read()

        # --- Master - Root Define & Config ---
        # Connect Master
        self._master = master
        # Set Title Windows
        self._master.title(self.TEXTS['win_title'])
        # Set Icon
        self._master.iconbitmap(self._ICON)
        # Connect Theme Update Signal
        self._master.SIG_THEME_UPDATE.connect = {'LoginFrame': self.theme_update}
        # Set Geometry - Size
        self._master.geometry('350x620+20+20')
        # Set Minimum Size
        self._master.minsize(350, 620)
        # Set Maximum Size - `None`` Means No Size Limit
        self._master.maxsize(None, None)

        # --- Photo Place Holder ---
        self._photo: PhotoImage = None

        # --- Main Frame ---
        # Create Main Frame
        self._main_frame = ttk.Frame(self._master)
        # Packed To Master `Root`
        self._main_frame.pack(anchor='center')

        # --- Logo ---
        # Label Login
        self._lbl_logo = ttk.Label(
            self._main_frame,
            text=self.TEXTS['lbl_logo'],
            font=('poppins', '20', 'bold'),
            padding='0p, 10p, 0p, 10p'
            )
        self._lbl_logo.pack(side='top', anchor='n')

        # Avatar Label
        # NOTE: Add Image After Create Complete & Call Theme Update Calling `_avatar_chosing` method
        self._avatar = ttk.Label(
            self._main_frame,
            padding='0p, 0p, 0p, 0p'
        )
        self._avatar.pack(side='top', expand=True, fill='y', anchor='n', pady=10, ipady=10)

        # --- Input Frame ---
        # Input Frame
        self._input_frame = ttk.Frame(self._main_frame, padding='0p, 0p, 0p, 0p')
        self._input_frame.pack()

        # --- Input Widget ---
        # UserLabel
        self._lbl_user = ttk.Label(
            self._input_frame,
            text=self.TEXTS['lbl_username'],
            font=('poppins', '12', 'normal'),
            padding='0p, 0p, 0p, 0p'
            )
        self._lbl_user.pack()

        # UserInput > Entry
        self._inp_user = ttk.Entry(self._input_frame, width=40)
        self._inp_user.pack(pady=5)
        self._inp_user.focus()  # Set Focus Into Entry UserName

        # PasswordLabel
        self._lbl_password = ttk.Label(
            self._input_frame,
            text=self.TEXTS['lbl_password'],
            font=('poppins', '12', 'normal'),
            padding='0p, 0p, 0p, 0p'
            )

        self._lbl_password.pack()
        
        # PasswordInput > Entry
        self._inp_password = ttk.Entry(self._input_frame, width=40, show='●') # `●` Unicode Char `U+25CF`
        self._inp_password.pack(pady=5)

        # --- Buttons ---
        # Login
        self._btn_login = ttk.Button(
            self._input_frame,
            text=self.TEXTS['btn_login'],
            command=self._logedin,
            padding='0p, 0p, 0p, 0p'
            )
        self._btn_login.pack(pady=6)

        # Clear
        self._btn_clear = ttk.Button(
            self._input_frame,
            text=self.TEXTS['btn_clear'],
            command=self._clear,
            padding='0p, 0p, 0p, 0p'
            )
        self._btn_clear.pack(pady=10)

        # Create Account
        self._btn_create = ttk.Button(
            self._input_frame,
            text=self.TEXTS['btn_create_account'],
            command=self._create_account,
            padding='20p, 0p, 20p, 0p'
            )
        self._btn_create.pack(pady=8)

        # --- Information ---
        # FrameInfo
        self._info_frame = ttk.Frame(self._input_frame)
        self._info_frame.pack(anchor='center', expand=1, fill='y')
        
        # Check Button Color Reverse - Theme Color Mode Reverse `dark`>`light`, `light`>`dark`
        self._cbtn_color_change = ttk.Checkbutton(
            self._info_frame,
            text=self.TEXTS['cbtn_color_reverse'],
            state= 'normal',
            style='Switch.TCheckbutton', # NOTE: Switch Style 
            command=self.change_color_mode,
            padding='12p, 0p, 0p, 0p',
            )
        self._cbtn_color_change.grid(row=0, column=0, sticky='w', pady=20, padx=2)

        # Info
        self._lbl_comments = ttk.Label(
            self._info_frame,
            text=self.TEXTS['lbl_comments'],
            font=('poppins', '8', 'bold'),
            padding="0p, 0p 0p 0p",
            )
        self._lbl_comments.grid(row=1, column=0, pady=4)

        # About
        self._lbl_about = ttk.Label(
            self._info_frame,
            text=self.TEXTS['lbl_about'],
            font=('poppins', '7', 'bold'),
            padding="60p, 4p 10p 8p"
            )
        self._lbl_about.grid(row=2, column=1, sticky='se')

        # NOTE: 
        # Set Avator & Update Theme For Fixed Widget Packing
        # If Diactive This `Call` See Moved Widget After Change Color In Running 
        self.theme_update()

        # Access Actions
        self._action_act = Actions()

        # Connect Actions Error Signal --> `backend_login`
        self._action_act.ERROR_SIGNAL.connect = self._message

    def change_comments_txt(self, comments: str) -> None:
        # Runtime Change Comments
        # NOTE: This Comments Forget After Closed Windows & Back To Default Comments.
        # ^ For Chang Default Text Change `lbl_comments` in `TEXT` Dictinary
        self._lbl_comments.configure(text= comments)
        print('Label Comments `Text` is Changed')

    def theme_update(self) -> None:
        # After First Running This Method Is Call & Fixing Posistion Widget
        # NOTE: if Disable This Method If Changed Color Or Other Changing Theme Widget Position Changes !!!
        # After Theme Changed Or Color Changed This Method Is Call
        self._main_frame.pack_forget()

        # Set Avatar
        self._avatar_choser()

        # Label Color Set Color
        self._fixed_lable_color()

        self._main_frame.pack()

    def change_color_mode(self) -> None:
        # CheckBox Color Changes
        color_revers = self._reverse_style_name()
        self._master.color_style = color_revers
        self._fixed_lable_color()

        print(f'COLOR REVERSE STYLE ACTION')

    def _reverse_style_name(self) -> str:
        # Reversed Color Style Get Activate Style & Reversed
        # Calling This Method From `change_color_mode`
        match self._master.color_style.value:
            case 'dark':
                return 'light'
            case 'light':
                return 'dark'

    def _message(self, act_name: ActionsNames, err: str) -> None:
        messagebox.showerror(f'- ACTION ERROR - {act_name.value.upper()}', message=err)

    def _avatar_choser(self) -> None:
        # Avatar Chosing With Color Style
        get_color_mode = self._master.color_style.value
        self._photo = PhotoImage(data=self._avatars_data[get_color_mode], format='png')
        self._avatar.configure(image=self._photo)

    def _fixed_lable_color(self) -> None:
        # Fixed Color Label
        # Get Root Color Mode
        get_color_mode = self._master.color_style.value

        # Set Color For Label From Color Table
        logo, comments, about = (
            self.COLOR_LABELS['lbl_logo'][get_color_mode],
            self.COLOR_LABELS['lbl_comments'][get_color_mode],
            self.COLOR_LABELS['lbl_about'][get_color_mode],
            )

        # Set Color Label
        self._lbl_logo.configure(foreground=logo)
        self._lbl_comments.configure(foreground=comments)
        self._lbl_about.configure(foreground=about)

    def _logedin(self) -> None:
        username = None if self._inp_user.get().isspace() else self._inp_user.get()
        password = None if self._inp_password.get().isspace() else self._inp_password.get()

        # NOTE: See Actions in `actions.py`
        check = self._action_act.btn_login(username, password)

        if check:
            self._clear()
            messagebox.showinfo('Welcome', message=f"Dear {username} Welcome !")

    def _clear(self) -> None:
        # Clear UserName & Password Entry Feild
        self._inp_user.delete(0, 'end')
        self._inp_password.delete(0, 'end')

        # Set Focus User Input `Entry`
        self._inp_user.focus()

        print("BTN <CLEAR> IS CLICKED")

    def _create_account(self) -> None:
        # Get Input UserName & Password if `isspace` set `None`
        username = None if self._inp_user.get().isspace() else self._inp_user.get()
        password = None if self._inp_password.get().isspace() else self._inp_password.get()

        # Create Account  --> see `Actions` module `create_account` method
        created = self._action_act.btn_create_account(username, password)

        if created:
            self._clear()
            messagebox.showinfo('Account Is Created', message=f"User [{username}] is Created.")



__dir__ = ('LoginFrame',)
