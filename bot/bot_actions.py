from utils.screen_capture import ScreenCapture
from utils.image_processing import ImageProcessor
from utils.utils import Utils
from bot.bot_controller import BotController
from bot.bot_data import BotData
from utils.delay_manager import DelayManager

class BotActions:
    def __init__(self, data: BotData):
        self.data = data
        self.triggerbot = False
        self.exit_program = False
        self.bot_controller = BotController(data.trigger_hotkey, data.exit_hotkey)
        self.screen_capture = ScreenCapture()
        self.image_processor = ImageProcessor(data.color_tolerance, data.threshold, *data.color)
        self.delay_manager = DelayManager(data.base_delay, data.random_delay)
        
    def searcher_in_o(self):
        img = self.screen_capture.capture()
        is_found = self.image_processor.process(img)
        
        #print(self.triggerbot, len(matching_pixels), self.data.threshold)
        if self.triggerbot and is_found:
            self.delay_manager.make_shoot_delay()
            self.bot_controller.shoot()

    def hold(self):
        while True:
            if self.bot_controller.is_trigger_hotkey_pressed():
                self.triggerbot = True
                self.searcher_in_o()
            else:
                self.delay_manager.make_check_delay()
            if self.bot_controller.is_exit_hotkey_pressed():
                print("trigger hold mode exit")
                self.exit_program = True
                Utils.exiting()

    def starter(self):
        while not self.exit_program:
            self.hold()
