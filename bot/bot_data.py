# bot_data.py
class BotData:
    def __init__(self, trigger_hotkey, exit_hotkey, trigger_delay, base_delay, color_tolerance, threshold, color):
        self.trigger_hotkey = trigger_hotkey
        self.exit_hotkey = exit_hotkey
        self.trigger_delay = trigger_delay
        self.base_delay = base_delay
        self.color_tolerance = color_tolerance
        self.threshold = threshold
        self.color = color  # (R, G, B)
