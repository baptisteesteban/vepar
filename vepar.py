#!/usr/bin/env python
import sys
import os
from glob import glob
import re
import shutil

import numpy as np
import matplotlib.pyplot as plt
from skimage import io
from tqdm import tqdm

from argument import parse_argument
from convert import convert

if __name__ == "__main__":
    args = parse_argument()
        
    print("[+] Initialization")
    filenames = glob(args.input + "/*.pgm")
    filenames = sorted(filenames, key=lambda f: int(re.sub('\D', '', f)))
    
    if args.save_ppm:
        if os.path.exists("./resulting_ppm"):
            shutil.rmtree("./resulting_ppm")            
        os.mkdir("./resulting_ppm")
        
    print("[+] Processing")
    for i in tqdm(range(len(filenames))):
        filename = filenames[i]
        image_out = convert(filename)
        if args.save_ppm:
            io.imsave("./resulting_ppm/" + str(re.sub('\D', '', filename)) + ".ppm", image_out)
        else:
            plt.title(filename)
            plt.imshow(image_out)
            plt.draw()
            plt.pause(1 / args.cadence)
            plt.clf()
    
    