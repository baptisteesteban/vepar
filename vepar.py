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
from vepar_file import VeparFile

if __name__ == "__main__":
    args = parse_argument()
        
    print("[+] Initialization")
    filenames = glob(args.input + "/*.pgm")
    filenames = sorted(filenames, key=lambda f: int(re.sub('\D', '', f)))
    
    vepar_file_info = None
    if len(args.config) > 0:
        print("[+] Parsing vepar file")
        vepar_file_info = VeparFile.parse_file(args.config)
    
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
            
    print("[+] End")
    
    