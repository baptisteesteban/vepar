import argparse

def parse_argument():
    parser = argparse.ArgumentParser(prog="vepar", description="Utility for MPEG-2")
    parser.add_argument("input", type=str, help="The input directory")
    parser.add_argument("--save-ppm", help="Save the images in ppm format. The input value is the save directory", default="")
    return parser.parse_args()