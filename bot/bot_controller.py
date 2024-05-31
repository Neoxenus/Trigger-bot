import win32api
import mouse
import keyboard
class BotController:
    def __init__(self, trigger_hotkey, exit_hotkey):
        self.trigger_hotkey = trigger_hotkey
        self.exit_hotkey = exit_hotkey

    def is_trigger_hotkey_pressed(self):
        return win32api.GetAsyncKeyState(self.trigger_hotkey) < 0

    def is_exit_hotkey_pressed(self):
        return win32api.GetAsyncKeyState(self.exit_hotkey) < 0
    def shoot(self):
        print("enemy is found")
        #keyboard.press_and_release("k")
        mouse.click()
