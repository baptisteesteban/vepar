import argparse

def parse_argument():
    parser = argparse.ArgumentParser(prog="vepar", description="Utility for MPEG-2")
    parser.add_argument("input", type=str, help="The input directory")
    parser.add_argument("--visualize", help="Visualize the video after treatment", action="store_true")
    parser.add_argument("--cadence", help="Number of image shown by second", type=int, default=100)
    parser.add_argument("--config", help="The vepar file exported from mpeg2dec", type=str, default="")
    return parser.parse_args()