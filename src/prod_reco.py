# Jamar Fraction
# CPTS 315
# PA3


IN_FILE = ''
OUT_FILE = './output.txt'


# Read in the file
def read_input():
    with open(IN_FILE, "r") as text_file:
        all_lines = text_file.readlines()

    return all_lines


# file dumping
def dump_output(user_recommendations):
    with open(OUT_FILE, "w") as text_file:
        pass

    return


def main():
    # Read the input file
    print("Reading data")
    all_lines = read_input()
    print("Done")


if __name__ == '__main__':
    main()
