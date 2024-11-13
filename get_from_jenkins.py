from argparse import ArgumentParser
import requests
from requests.auth import HTTPBasicAuth
import os


def main(user: str, password: str):

    url="https://jenkins/output.zip"
    filename = "downloaded_file"
    split = os.path.split(url)
    if len(split) == 2:
        filename = split[1]

    basic = HTTPBasicAuth(user, password)

    response = requests.get(url, auth=basic)

    # Check if the request was successful
    if response.status_code == 200:
        # Open the file in binary write mode and save the response content
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:  # Filter out keep-alive chunks
                    file.write(chunk)

        print(f"File downloaded successfully and saved as {filename}")
    else:
        print(f"Failed to download the file. Status code: {response.status_code}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--password", type=str, required=True)
    parser.add_argument("--user", type=str, required=True)

    args = parser.parse_args()

    main(**vars(args))
