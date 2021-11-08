import argparse


def getUserName(username):
    print("Getting username from command line")
    if username == "jake":
        print("Valid username")
    else:
        print("invalid username")


def findSubstring(masterString, subString):
    if masterString.__contains__(subString):
        print(f"{subString} present in {masterString}")
    else:
        print("Not found")


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", type=str, required=True, help="please enter username")
    parser.add_argument('--masterString', type=str, required=True, help="please enter master string")
    parser.add_argument("--subString", type=str, required=True)
    args = parser.parse_args()
    getUserName(args.username)
    findSubstring(args.masterString, args.subString)
