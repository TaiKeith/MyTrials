import sys

if __name__ == "__main__":
    argv = sys.argv
    n = len(argv) - 1

    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
    else:
        print("{} arguments:".format(n))
    i = 1
    for arg in argv[1:]:
        print("{}: {}".format(i, arg))
        i += 1
