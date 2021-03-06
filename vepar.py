#!/usr/bin/env python
import os
from glob import glob
import re
import shutil

from skimage import io
from tqdm import tqdm

from argument import parse_argument
from convert import convert
from vepar_file import VeparFile
from bob import bob_deinterlace
from visualize import Visualization

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

    print("[+] Configure output ppm directory")
    if os.path.exists("./resulting_ppm"):
        shutil.rmtree("./resulting_ppm")
    os.mkdir("./resulting_ppm")

    print("[+] Processing")
    for i in tqdm(range(len(filenames))):
        filename = filenames[i]
        image_out = convert(filename)
        flag = vepar_file_info.ls_flags[i] if vepar_file_info else None
        frame1, frame2 = bob_deinterlace(image_out, flag)
        io.imsave("./resulting_ppm/" + str(re.sub('\D', '', filename)) + "_1.ppm", frame1)
        io.imsave("./resulting_ppm/" + str(re.sub('\D', '', filename)) + "_2.ppm", frame2)


    if args.visualize:
        v = Visualization(cadence_ips)
        v.visualize()

    print("[+] End")
