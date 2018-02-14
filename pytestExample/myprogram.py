import sys

def doubleit(x):
    if not isinstance(x, (int, float)):
        raise TypeError

    var = x * 2
    return var


def doublelines(filename):
    with open(filename) as f:
        newlist = [str(doubleit(int(val))) for val in f]
    with open(filename, "w") as f:
        f.write("\n".join(newlist))

if __name__ == "__main__":
    input_val = int(sys.argv[1])
    doubled_val = doubleit(input_val)

    print("the value of {0} is {1}".format(input_val, doubled_val))
