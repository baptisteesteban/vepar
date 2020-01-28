import matplotlib.pyplot as plt
import matplotlib.animation as anim

from skimage import io
from glob import glob
import re
   
class Visualization:
    def __init__(self, interval=50):
        self.i = 1
        self.filenames = sorted(glob("./resulting_ppm/*.ppm"), key=lambda f: int(re.sub('\D', '', f)))
        self.interval = interval
        
    def update(self, *args):
        if self.i == len(self.filenames):
            self.i = 0
        self.im.set_array(io.imread(self.filenames[self.i]))
        self.i += 1
        return self.im
    
    def visualize(self):
        fig, ax = plt.subplots()
        self.im = ax.imshow(io.imread(self.filenames[0]))
        ani = anim.FuncAnimation(fig, self.update, interval=self.interval)
        plt.show()
        