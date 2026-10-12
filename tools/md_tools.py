import argparse
import glob
from pathlib import Path
from typing import Optional


def get_files_as_drawings(dir_path: str, width: Optional[int] = None, height: Optional[int] = None):

    if not any([width, height]):
        raise RuntimeError("Width or height must be given")

    dir_path = Path(dir_path)
    files = glob.glob(str(dir_path / "*"))

    width_height = ""
    if width:
        width_height += f'width="{width}" '
    if height:
        width_height += f'height="{height}" '

    for f in files:
        msg = f'<img src="{f}" alt="drawing" {width_height}/>'
        print(msg)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--dir_path", type=str, required=True, help="Path to dir with files")
    parser.add_argument("-w", "--width", type=int, help="Width of image in pix")
    parser.add_argument("-he", "--height", type=int, help="Height of image in pix")

    args = parser.parse_args()

    get_files_as_drawings(args.dir_path, width=args.width, height=args.height)


if __name__ == "__main__":
    main()

