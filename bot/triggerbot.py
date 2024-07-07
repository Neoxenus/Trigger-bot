# triggerbot.py
#from config_manager import ConfigManager
from bot.bot_data import BotData
from bot.bot_actions import BotActions

from bot.bot_data_loader import BotDataLoader
from utils.utils import Utils

class TriggerBot:
    def __init__(self):
        print("initialization")

        bot_data_loader = BotDataLoader()
        try:
            bot_data = bot_data_loader.load_bot_data()
        except Exception:
            Utils.exiting()

        self.bot_actions = BotActions(bot_data)
        
        print("bot is started")

    def starter(self):
        self.bot_actions.starter()