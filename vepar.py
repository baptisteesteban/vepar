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
from bob import bob_deinterlace

if __name__ == "__main__":
    args = parse_argument()
        
    print("[+] Initialization")
    filenames = glob(args.input + "/*.pgm")
    filenames = sorted(filenames, key=lambda f: int(re.sub('\D', '', f)))
    
    vepar_file_info = None
    cadence_ips = 25
    if len(args.config) > 0:
        print("[+] Parsing vepar file")
        vepar_file_info = VeparFile.parse_file(args.config)
        if vepar_file_info.frame_period:
            cadence_ips = 27000000 // vepar_file_info.frame_period
        print(str(vepar_file_info))
    
    if args.save_ppm:
        if os.path.exists("./resulting_ppm"):
            shutil.rmtree("./resulting_ppm")            
        os.mkdir("./resulting_ppm")
        
    print("[+] Processing")
    for i in tqdm(range(len(filenames))):
        filename = filenames[i]
        image_out = convert(filename)
        frame1, frame2 = bob_deinterlace(image_out, None)
        if args.save_ppm:
            io.imsave("./resulting_ppm/" + str(re.sub('\D', '', filename)) + "_1.ppm", frame1)
            io.imsave("./resulting_ppm/" + str(re.sub('\D', '', filename)) + "_2.ppm", frame2)
        else:
            plt.imshow(frame1)
            plt.draw()
            plt.pause(1 / args.cadence)
            plt.clf()
            plt.imshow(frame1)
            plt.draw()
            plt.pause(1 / args.cadence)
            plt.clf()
            
    print("[+] End")
    
    