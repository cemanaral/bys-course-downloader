import sys

def main(username, password):
    print("username: " + username)
    print("password: " + password)




if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("Invalid Input\nUsage: python bys.py username password")

    main(username=sys.argv[1], password=sys.argv[2])