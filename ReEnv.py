import win32api,win32gui,win32con
win32api.SendMessage(win32con.HWND_BROADCAST,win32con.WM_SETTINGCHANGE,0,"Environment");
