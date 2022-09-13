from typing import Tuple
import numpy as np
import matplotlib.pyplot as plt


class Canvas():

    def __init__(self, size=(640, 480), viewport_size=(1., 1.), proj_plane_dist=1):
        self.size = size
        self.viewport_size = viewport_size
        self.proj_plane_dist = 1

        self.__canvas = np.zeros((self.height, self.width, 3), dtype=np.uint8)

    @property
    def width(self):
        return self.size[0]
    
    @property
    def height(self):
        return self.size[1]

    def put_pixel(self, row: int, col: int, color: Tuple[int]=(0, 0, 0)) -> None:
        if 0 <= row < self.height and 0 <= col < self.width:
            self.__canvas[row, col, :] = color

    def canvas_to_viewport(self, row, col):
        x = self.viewport_size[0] * (col - self.width / 2) / self.width
        y = - self.viewport_size[1] * (row - self.height / 2) / self.height
        return np.array([x, y, self.proj_plane_dist])

    def show(self):
        fig = plt.figure()
        fig.canvas.set_window_title('')
        plt.imshow(self.__canvas)
        plt.xticks([])
        plt.yticks([])
        plt.gca().set_aspect(1)
        plt.show()