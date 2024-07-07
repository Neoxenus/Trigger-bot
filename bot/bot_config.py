# bot_config.py
from ctypes import WinDLL

user32, shcore = (
    WinDLL("user32", use_last_error=True),
    WinDLL("shcore", use_last_error=True),
)

shcore.SetProcessDpiAwareness(2)
WIDTH, HEIGHT = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]

class BotConfig:
    ZONE = 4
    GRAB_ZONE = (
        int(WIDTH / 2 - ZONE),
        int(HEIGHT / 2 - ZONE),
        int(WIDTH / 2 + ZONE),
        int(HEIGHT / 2 + ZONE)
    )
    # def get_grab_zone():
    #     return GRAB_ZONE
