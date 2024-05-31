import time
from utils.screen_capture import ScreenCapture
from utils.image_processing import ImageProcessor
from utils.utils import exiting
from bot.bot_controller import BotController
from bot.bot_data import BotData

class BotActions:
    def __init__(self, data: BotData, grab_zone):
        self.data = data
        self.triggerbot = False
        self.exit_program = False
        self.bot_controller = BotController(data.trigger_hotkey, data.exit_hotkey)
        self.screen_capture = ScreenCapture(grab_zone)
        self.image_processor = ImageProcessor(data.color_tolerance, data.threshold, *data.color)
        
    def searcher_in_o(self):
        img = self.screen_capture.capture()
        matching_pixels = self.image_processor.process(img)
        
        #print(self.triggerbot, len(matching_pixels), self.data.threshold)
        if self.triggerbot and len(matching_pixels) > self.data.threshold:

            delay_percentage = self.data.trigger_delay / 100.0
            actual_delay = self.data.base_delay + self.data.base_delay * delay_percentage
            # time.sleep(actual_delay)
            self.bot_controller.shoot()

    def hold(self):
        while True:
            if self.bot_controller.is_trigger_hotkey_pressed():
                self.triggerbot = True
                self.searcher_in_o()
            else:
                time.sleep(0.1)
            if self.bot_controller.is_exit_hotkey_pressed():
                print("trigger hold mode exit")
                self.exit_program = True
                exiting()

    def starter(self):
        while not self.exit_program:
            self.hold()
