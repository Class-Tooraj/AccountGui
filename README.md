#### IN THE NAME OF GOD

---

# Modern Account Gui

Modern Theme Support Gui Application . Use `Tkinter` & `Python` For Structure Gui and Backend Programing.

For Run Only You Need `Python 3.10`

*LICENSE :* `MIT`



**Account App Structure :**

> ***Gui :***
> 
> > **path :** <DIR>/source/account_gui/...
> > 
> > **CustomTk :** This Mudole Instanse `tkinter.Tk` for Supporting Theme.
> > 
> > **LoginFrame :** This Mudole is Login Windows
> > 
> > All Gui Widget in This Directory.
> 
> ***Themes :***
> 
> > **path :** <DIR>/source/themes/...
> > 
> > **Style :** Dark, Light
> > 
> > **Azure :** Tcl Custom Themes
> > 
> > **Sun-Valley :** Tcl Custom Themes
> > 
> > All Themes in This Directory.
> 
> ***Image :***
> 
> > **path :** <DIR>/source/img/...
> > 
> > **avatars :** Supports `dark` and `light`
> > 
> > All image in This Directory.
> 
> ***Backend :***
> 
> > **path :** <DIR>/source/aacount_backend/...
> > 
> > **Actions :** Action Login and Create Account Buttons
> > 
> > All Code & Exceptions in This Directory.



**Run and Test :**

After Download

1 . Create VirtualEnvirements.

```bash
python3 -m venv ./venv
```

2 . Activate VirtualEnvirements.

```bash
./venv/Scripts/activate.bat
```

3 . Run `main.py`.

```bash
python3 main.py
```

Enjoy The Show :)



**In App :**

Type UserName & Password then Clicked `CreateAccount` Button Create Very Simple Json File And Store UserName & Password then See Message Account Created.

After Created Account Type UserName & Password then Clicked `Login` Button See The Welcome MessageBox.



When You Want Reverse Color Style RunTime Click `ColorReverse` Button.



**Use For Real App :**

Must Created Frame For Account Creator & Connect Account To Your Database.

I tried to put the description in the code so that someone who is going to use it and change it can more easily understand what happened.



**Theme Supprots :**

Frist Read Tcl Themes And Then Call Tcl `eval` Command For Execute Tcl Themes.

For Create Frame & Widgets Supporting Theme Use `tkinter.ttk` Widgets Becuse Tkinter Widgets Not Suporting Themes.

```python
from tkinter import ttk
```

If you Want Replace Tkinter Regular Widget To Themes Support Widgets Use This Command

```python
from tkinter import *
from tkinter.ttk import *
```

Themes Source:

**Azure :** [GitHub - rdbende/Azure-ttk-theme: Azure theme is a beautiful and modern ttk theme, inspired by Fluent design](https://github.com/rdbende/Azure-ttk-theme)

**Sun-Valley :** [GitHub - rdbende/Sun-Valley-ttk-theme: A stunning theme for ttk, based on Microsoft&#39;s Sun Valley visual style](https://github.com/rdbende/Sun-Valley-ttk-theme)

This App Use `Gif` Format Themes Available The Source Themes.

---

**Screen Shot :**



**Azure**

![](D:\TkGuiPythonProject\Login\screenshots\azure.png)



**Sun-Valley**

![](D:\TkGuiPythonProject\Login\screenshots\sun-valley.png)



**Azeru & Sun-Valley**

![](D:\TkGuiPythonProject\Login\screenshots\all.png)

---

**AUTHOR :** ***ToorajJahangiri***
