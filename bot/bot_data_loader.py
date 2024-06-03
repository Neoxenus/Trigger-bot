# bot_data_loader.py
import json
from bot.bot_data import BotData

class BotDataLoader:
    def __init__(self, config_path='resourses/config.json'):
        self.config_path = config_path

    def load_bot_data(self):
        with open(self.config_path) as jsonFile:
            data = json.load(jsonFile)
        try:
            bot_data = BotData(
                trigger_hotkey=int(data["trigger_hotkey"], 16),
                exit_hotkey=int(data["exit_hotkey"], 16),
                random_delay=data["random_delay"],
                base_delay=data["base_delay"],
                color_tolerance=data["color_tolerance"],
                threshold=data["threshold"],
                color=data["rgb"]
            )
            return bot_data
        except KeyError as e:
            print(f"Configuration key error: {e}")
            raise
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise
