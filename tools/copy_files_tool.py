import argparse
import glob
import os
import shutil


def copy_all_files_together(root_dir: str, levels: int, suffix: str, output: str = "output",
                            path_in_name: bool = False):

    stages = [root_dir,]
    stages.extend(["*"] * levels)

    if suffix.startswith("."):
        suffix = suffix[1:]
    stages.append(f"*.{suffix}")

    path = os.path.join(*stages)

    files = glob.glob(path)
    os.makedirs(output, exist_ok=True)
    for f in files:

        if path_in_name:
            output_name = "___".join(f.split(os.path.sep)[-(levels+1):])
        else:
            output_name = os.path.basename(f)
        shutil.copy(f, os.path.join(output, output_name))


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--root-dir", type=str, required=True, help="Root dir")
    parser.add_argument("--levels", type=int, required=True, help="Number of 'inside' directories")
    parser.add_argument("--output", type=str, default="output", help="Directory with results")
    parser.add_argument("--suffix", type=str, default="jpg", help="Suffix of files")
    parser.add_argument("--full-path", action="store_true", help="Output filenames contain full path of origin")

    args = parser.parse_args()

    copy_all_files_together(args.root_dir, args.levels, args.suffix, args.output, args.full_path)


if __name__ == "__main__":
    main()