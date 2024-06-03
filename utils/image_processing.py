import numpy as np
class ImageProcessor:
    def __init__(self, color_tolerance, threshold, R, G, B):
        self.color_tolerance = color_tolerance
        self.threshold = threshold
        self.R = R
        self.G = G
        self.B = B

    def process(self, img):
        # #old color mask
        # pixels = img.reshape(-1, 4)
        # color_mask = (
        #     (pixels[:, 0] > self.R - self.color_tolerance) & (pixels[:, 0] < self.R + self.color_tolerance) &
        #     (pixels[:, 1] > self.G - self.color_tolerance) & (pixels[:, 1] < self.G + self.color_tolerance) &
        #     (pixels[:, 2] > self.B - self.color_tolerance) & (pixels[:, 2] < self.B + self.color_tolerance)
        # )
        # matching_pixels = pixels[color_mask]
        # return len(matching_pixels) > self.threshold

        img_array = np.array(img, dtype=np.float32)
        
        # Extract the RGB channels
        pixels = img_array.reshape(-1, 4)[:, :3]
        target_color = np.array([self.R, self.G, self.B], dtype=np.float32)
        
        # Calculate the Euclidean distance between each pixel and the target color
        color_diff = np.sqrt(np.sum((pixels - target_color) ** 2, axis=1))
        #print(color_diff)
        # Create a mask where the distance is less than the threshold
        mask = color_diff < self.color_tolerance
        
        # Count the number of matching pixels
        matching_pixels = pixels[mask]

        print(pixels[0, 0:3])
        return len(matching_pixels) > self.threshold
