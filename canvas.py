from typing import Tuple

import cv2
import numpy as np
from PIL import Image


class Canvas():

    def __init__(self, size=(600, 600), viewport_size=(1., 1.), proj_plane_dist=1):
        self.size = size
        self.viewport_size = viewport_size
        self.proj_plane_dist = proj_plane_dist

        self.__canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)

    @property
    def width(self):
        return self.size[0]
    
    @property
    def height(self):
        return self.size[1]

    def put_pixel(self, row: int, col: int, color: Tuple[int, int, int]=(0, 0, 0)) -> None:
        if 0 <= row < self.height and 0 <= col < self.width:
            row = self.height - row - 1
            self.__canvas[row, col, :] = color

    def canvas_to_viewport(self, row: int, col: int):
        x = self.viewport_size[0] * (col - self.width / 2) / self.width
        y = self.viewport_size[1] * (row - self.height / 2) / self.height
        return np.array([x, y, self.proj_plane_dist])

    def show(self):
        cv2.imshow("", self.__canvas[..., ::-1])
        cv2.waitKey(0)
