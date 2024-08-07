import numpy as np
from mss import mss
from bot.bot_config import BotConfig
import mss.tools

class ScreenCapture:
    def __init__(self):
        self.grab_zone = BotConfig.GRAB_ZONE

    def capture(self):
        with mss.mss() as sct:
            img = np.array(sct.grab(self.grab_zone))

            # Save the picture
            #output = "example.png".format(self.grab_zone)
            #sct_img = sct.grab(self.grab_zone)
            #mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            #print(output)

            return img
