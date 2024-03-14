import os
import json
import argparse


JUPYTERPATH=".local/share/jupyter/kernels/venv_current"
KERNELFILE="kernel.json"


def get_setup(user: str) -> dict:
    with open(os.path.join(get_jupyter_path(user), KERNELFILE)) as f:
        setup = json.load(f)
    return setup


def save_setup(setup: dict, user: str):
    with open(os.path.join(get_jupyter_path(user), KERNELFILE), "w") as f:
        json.dump(setup, fp=f)

        print(f"Setup changed for: {setup['argv'][0]}")


def get_jupyter_path(user: str) -> str:
    return os.path.join("/home", user, JUPYTERPATH)


def get_full_new_venv_path(venv_path: str) -> str:
    return os.path.join(os.path.abspath(venv_path), "bin", "python")


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--venv-path", help="Path to venv", default="venv")
    parser.add_argument("--user", help="User name")

    args = parser.parse_args()

    setup = get_setup(args.user)

    new_venv_path = get_full_new_venv_path(args.venv_path)
    if not os.path.exists(new_venv_path):
        raise ValueError(f"Path {new_venv_path} does not exist.")

    setup["argv"][0] = new_venv_path

    save_setup(setup, args.user)


if __name__ == "__main__":
    main()
