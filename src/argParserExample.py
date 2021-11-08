import argparse


def getUserName(username):
    print("Getting username from command line")
    if username == "jake":
        print("Valid username")
    else:
        print("invalid username")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", type=str, required=True, help="please enter username")
    args = parser.parse_args()
    getUserName(args.username)
