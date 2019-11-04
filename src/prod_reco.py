# Jamar Fraction
# CPTS 315
# PA3


STOP_LIST = '../data/fortune-cookie-data/stoplist.txt'
TRAIN_DATA = '../data/fortune-cookie-data/traindata.txt'
TRAIN_LABELS = 'data/fortune-cookie-data/trainlabels.txt'
OUT_FILE = './output.txt'


# Read in the file
def read_input(file):
    with open(file, "r") as text_file:
        all_lines = text_file.read().splitlines()

    return all_lines


# file dumping
def dump_output(user_recommendations):
    with open(OUT_FILE, "w") as text_file:
        pass

    return


def build_vocabulary(training_lines, stop_list):

    # create a set of all the words in the fortune cookies that are not stop words
    print("Cleaning vocabulary")
    vocabulary = sorted(
        list(set([word for sentence in training_lines for word in sentence.split() if word not in stop_list])))
    print("done")

    return vocabulary


def create_feature_vectors(training_lines, vocabulary, stop_list):
    feature_vectors = []

    # split the training lines to a list of lists of strings
    split_lines = [line.split() for line in training_lines]

    for line in split_lines:

        current_vector = []

        # if the current word in the vocab is in the current line, append a 1, if not, append a zero
        # this produces a vector of size len(vocab), where the ith index of the vector will be a 1 if the ith word in
        # vocab is present in the current line
        for word in vocabulary:
            current_vector.append(1) if word in line else current_vector.append(0)

        feature_vectors.append(current_vector)

    # return the fruits of our labor
    return feature_vectors


def main():
    # Fortune Cookie classification

    # Pre-process steps
    # ********************************************************
    # Read in the training data
    print("Reading training data")
    training_lines = read_input(TRAIN_DATA)
    print("Done")

    # Read in the stop list
    print("Reading stop list")
    stop_list = read_input(STOP_LIST)
    print("Done")

    print("Building vocabulary")
    vocabulary = build_vocabulary(training_lines, stop_list)
    print("Done building vocabulary")

    # Create feature vectors
    print("Creating feature vectors")
    feature_vectors = create_feature_vectors(training_lines=training_lines, vocabulary=vocabulary, stop_list=stop_list)
    print("Done")


if __name__ == '__main__':
    main()
