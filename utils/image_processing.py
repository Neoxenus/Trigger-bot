# image_processing.py
import numpy as np

class ImageProcessor:
    def __init__(self, color_tolerance, threshold, R, G, B):
        self.color_tolerance = color_tolerance
        self.threshold = threshold
        self.R = R
        self.G = G
        self.B = B

    def process(self, img):
        pixels = img.reshape(-1, 4)
        color_mask = (
            (pixels[:, 0] > self.R - self.color_tolerance) & (pixels[:, 0] < self.R + self.color_tolerance) &
            (pixels[:, 1] > self.G - self.color_tolerance) & (pixels[:, 1] < self.G + self.color_tolerance) &
            (pixels[:, 2] > self.B - self.color_tolerance) & (pixels[:, 2] < self.B + self.color_tolerance)
        )
        matching_pixels = pixels[color_mask]
        print(pixels[0, 0:3])
        return matching_pixels
