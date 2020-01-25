#!/usr/bin/env python
import sys

import numpy as np
import matplotlib.pyplot as plt

from argument import parse_argument
from convert import convert
from glob import glob
import re

if __name__ == "__main__":
    args = parse_argument()
        
    filenames = glob(args.input + "/*.pgm")
    filenames = sorted(filenames, key=lambda f: int(re.sub('\D', '', f)))
    print(type(filenames))
    for filename in filenames:
        image_out = convert(filename)
        if len(args.save_ppm) > 0:
            io.imsave(args.save_ppm, image_out)
        else:
            plt.title(filename)
            plt.imshow(image_out)
            plt.show()
    
    